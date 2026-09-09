import android.content.Intent;
import android.content.ComponentName;
import android.os.Parcelable;
import android.os.Parcel;
import org.json.JSONObject;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.lang.reflect.Method;
import java.util.Iterator;

public class CoreProvision {
  public static void main(String[] args) {
    try { run(args); }
    catch (Exception e) { System.err.println("Provisioning failed (" + e.getClass().getSimpleName() + "); no payload values logged."); System.exit(1); }
  }
  private static void run(String[] args) throws Exception {
    if(args.length != 2 || (!args[1].equals("check") && !args[1].equals("launch")))
      throw new IllegalArgumentException("Usage: CoreProvision payload.json check|launch");
    if(Files.size(Paths.get(args[0])) > 65536) throw new IllegalArgumentException("Payload too large");
    JSONObject root = new JSONObject(new String(Files.readAllBytes(Paths.get(args[0])), "UTF-8"));
    String key = "android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE";
    JSONObject data = root.getJSONObject(key);
    String admin = "com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver";
    if(!admin.equals(root.optString("android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME")))
      throw new IllegalArgumentException("Unexpected admin component");
    String[] required = {"account", "accountType", "timestamp", "signature", "type"};
    if(data.length()!=required.length) throw new IllegalArgumentException("Unexpected schema");
    for(String k:required) if(!(data.opt(k) instanceof String) || data.getString(k).trim().isEmpty())
      throw new IllegalArgumentException("Missing or invalid pairing field");
    if(!"sr25519".equals(data.getString("accountType")) || !"single".equals(data.getString("type")))
      throw new IllegalArgumentException("Unsupported pairing type");
    String timestamp=data.getString("timestamp");
    if(!timestamp.matches("[0-9]{1,16}")) throw new IllegalArgumentException("Invalid timestamp");
    long stamp=Long.parseLong(timestamp), now=System.currentTimeMillis();
    if(stamp < now-14400000L || stamp > now+300000L)
      throw new IllegalArgumentException("Timestamp outside recorded window");
    Class<?> pbClass = Class.forName("android.os.PersistableBundle");
    Object pb = pbClass.getConstructor().newInstance();
    for (Iterator<String> it=data.keys(); it.hasNext();) {
      String k=it.next();
      pbClass.getMethod("putString",String.class,String.class).invoke(pb,k,data.getString(k));
    }
    Intent intent = new Intent("android.app.action.PROVISIONING_SUCCESSFUL");
    intent.setComponent(new ComponentName("com.acurast.attested.executor.canary", "com.acurast.attested.executor.ui.MainActivity"));
    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
    intent.putExtra(key,(Parcelable)pb);
    Parcel p=Parcel.obtain(); intent.writeToParcel(p,0); p.setDataPosition(0);
    Intent roundTrip=Intent.CREATOR.createFromParcel(p); p.recycle();
    Object actual=roundTrip.getParcelableExtra(key);
    if (!pbClass.isInstance(actual)) throw new IllegalStateException("Bundle type changed");
    for (Iterator<String> it=data.keys(); it.hasNext();) {
      String k=it.next();
      if(!data.getString(k).equals(pbClass.getMethod("getString",String.class).invoke(actual,k))) throw new IllegalStateException("Roundtrip mismatch: "+k);
    }
    System.out.println("Verified typed provisioning bundle and all " + data.length()+" fields; no values logged.");
    Object am=Class.forName("android.app.ActivityManager").getMethod("getService").invoke(null);
    Class<?> iam=Class.forName("android.app.IActivityManager");
    Method launch=null;
    for(Method m:iam.getMethods()) if(m.getName().equals("startActivityAsUser")) launch=m;
    if(launch==null) throw new IllegalStateException("No launch API");
    String[] expected = {"android.app.IApplicationThread", "java.lang.String", "android.content.Intent",
      "java.lang.String", "android.os.IBinder", "java.lang.String", "int", "int",
      "android.app.ProfilerInfo", "android.os.Bundle", "int"};
    Class<?>[] t=launch.getParameterTypes();
    if(t.length!=expected.length) throw new IllegalStateException("Unexpected launch signature");
    for(int i=0;i<t.length;i++) if(!t[i].getName().equals(expected[i]))
      throw new IllegalStateException("Unexpected launch signature");
    System.out.println("Launch interface matches recorded shape; QR signature is NOT verified here.");
    if(args[1].equals("check")) {System.out.println("Check only: app not launched, settings unchanged.");return;}
    Object result=launch.invoke(am,null,"com.android.shell",intent,null,null,null,0,0,null,null,0);
    System.out.println("Activity launch result: "+result);
  }
}
