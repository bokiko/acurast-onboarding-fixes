import android.content.Intent;
import android.content.ComponentName;
import android.os.Parcelable;
import android.os.Parcel;
import org.json.JSONObject;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import java.lang.reflect.Method;
import java.util.Iterator;

public class CoreProvision {
  public static void main(String[] args) {
    try { run(args); }
    catch (Failure e) { System.err.println("Provisioning stopped: " + e.code + "; no payload values logged."); System.exit(1); }
    catch (Exception | LinkageError e) { System.err.println("Provisioning stopped: E_RUNTIME; no payload values logged."); System.exit(1); }
  }
  private static void run(String[] args) throws Exception {
    if(args.length != 2 || (!args[1].equals("check") && !args[1].equals("launch")))
      throw new Failure("E_USAGE");
    String input;
    try (InputStream in = Files.newInputStream(Paths.get(args[0]));
         ByteArrayOutputStream out = new ByteArrayOutputStream()) {
      byte[] buffer = new byte[4096];
      int count;
      while ((count = in.read(buffer)) != -1) {
        if (out.size() + count > 65536) throw new Failure("E_SIZE");
        out.write(buffer, 0, count);
      }
      input = out.toString("UTF-8");
    }
    JSONObject data = validatePayload(input, System.currentTimeMillis());
    String key = "android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE";
    // app_process uses shell UID on the primary Android user only.
    int uid = (Integer) Class.forName("android.os.Process").getMethod("myUid").invoke(null);
    int user = (Integer) Class.forName("android.app.ActivityManager").getMethod("getCurrentUser").invoke(null);
    requireUser(uid, user);
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
    if (!pbClass.isInstance(actual)) throw new Failure("E_BUNDLE_TYPE");
    for (Iterator<String> it=data.keys(); it.hasNext();) {
      String k=it.next();
      if(!data.getString(k).equals(pbClass.getMethod("getString",String.class).invoke(actual,k))) throw new Failure("E_ROUNDTRIP");
    }
    System.out.println("Verified typed provisioning bundle and all " + data.length()+" fields; no values logged.");
    Object am=Class.forName("android.app.ActivityManager").getMethod("getService").invoke(null);
    Class<?> iam=Class.forName("android.app.IActivityManager");
    String[] expected = {"android.app.IApplicationThread", "java.lang.String", "android.content.Intent",
      "java.lang.String", "android.os.IBinder", "java.lang.String", "int", "int",
      "android.app.ProfilerInfo", "android.os.Bundle", "int"};
    Method launch = findLaunch(iam, expected);
    System.out.println("Launch interface matches recorded shape; QR signature is NOT verified here.");
    if(args[1].equals("check")) {System.out.println("Check only: app not launched, settings unchanged.");return;}
    Object result=launch.invoke(am,null,"com.android.shell",intent,null,null,null,0,0,null,null,0);
    if (!(result instanceof Integer)) throw new Failure("E_LAUNCH_RESULT");
    requireLaunchSuccess((Integer) result);
    System.out.println("Activity start accepted (0); pairing and Hub online status still require verification.");
  }

  static JSONObject validatePayload(String input, long now) throws Exception {
    JSONObject root;
    JSONObject data;
    try {
      root = new JSONObject(input);
      data = root.getJSONObject("android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE");
    } catch (Exception e) { throw new Failure("E_JSON"); }
    String admin = "com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver";
    if (!admin.equals(root.opt("android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME")))
      throw new Failure("E_ADMIN");
    String[] required = {"account", "accountType", "timestamp", "signature", "type"};
    if (data.length() != required.length) throw new Failure("E_SCHEMA");
    for (String k : required)
      if (!(data.opt(k) instanceof String) || data.getString(k).trim().isEmpty()) throw new Failure("E_SCHEMA");
    if (!"sr25519".equals(data.getString("accountType")) || !"single".equals(data.getString("type")))
      throw new Failure("E_PAIRING_TYPE");
    String timestamp = data.getString("timestamp");
    if (!timestamp.matches("[0-9]{1,16}")) throw new Failure("E_TIMESTAMP");
    long stamp = Long.parseLong(timestamp);
    // Local sanity bound only. The Hub's actual expiry is checked separately.
    if (stamp < now - 14400000L || stamp > now + 300000L) throw new Failure("E_WINDOW");
    return data;
  }

  static Method findLaunch(Class<?> api, String[] expected) throws Failure {
    Method found = null;
    for (Method method : api.getMethods()) {
      if (!method.getName().equals("startActivityAsUser") || method.getReturnType() != int.class) continue;
      Class<?>[] types = method.getParameterTypes();
      if (types.length != expected.length) continue;
      boolean matches = true;
      for (int i = 0; i < types.length; i++)
        if (!types[i].getName().equals(expected[i])) { matches = false; break; }
      if (!matches) continue;
      if (found != null) throw new Failure("E_LAUNCH_API");
      found = method;
    }
    if (found == null) throw new Failure("E_LAUNCH_API");
    return found;
  }

  static void requireLaunchSuccess(int result) throws Failure {
    // Only the observed START_SUCCESS result is accepted. Other outcomes require inspection.
    if (result != 0) throw new Failure("E_LAUNCH_RESULT");
  }

  static void requireUser(int uid, int user) throws Failure {
    if (uid != 2000 || user != 0) throw new Failure("E_USER");
  }

  static class Failure extends Exception {
    final String code;
    Failure(String code) { super(code); this.code = code; }
  }
}
