import org.json.JSONObject;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.charset.StandardCharsets;
import java.io.ByteArrayOutputStream;

// Host-only checks. Android parcel, permissions and launch are NOT simulated here.
public class CoreProvisionTest {
  static final long NOW = 1800000000000L;
  static int checks;
  interface Action { void run() throws Exception; }
  static void rejects(String code, Action action) throws Exception {
    try { action.run(); throw new AssertionError("Expected " + code); }
    catch (CoreProvision.Failure e) {
      if (!code.equals(e.code)) throw new AssertionError("Wrong error code");
      checks++;
    }
  }
  static JSONObject data() throws Exception {
    return new JSONObject().put("account", "SYNTHETIC-ACCOUNT")
      .put("accountType", "sr25519").put("timestamp", Long.toString(NOW))
      .put("signature", "SYNTHETIC-SIGNATURE").put("type", "single");
  }
  static String root(JSONObject data) throws Exception {
    return new JSONObject().put("android.app.extra.PROVISIONING_DEVICE_ADMIN_COMPONENT_NAME",
      "com.acurast.attested.executor.canary/com.acurast.attested.executor.lockdown.LockdownDeviceAdminReceiver")
      .put("android.app.extra.PROVISIONING_ADMIN_EXTRAS_BUNDLE", data).toString();
  }
  public interface Overloads {
    int startActivityAsUser(String value);
    int startActivityAsUser(int value);
  }
  static void rejectsProcess(String code, String contents, String mode) throws Exception {
    Path file = Files.createTempFile("core-synthetic-test-", ".json");
    try {
      Files.write(file, contents.getBytes(StandardCharsets.UTF_8));
      Process child = new ProcessBuilder(System.getProperty("java.home") + "/bin/java", "-cp",
        System.getProperty("java.class.path"), "CoreProvision", file.toString(), mode)
        .redirectErrorStream(true).start();
      ByteArrayOutputStream output = new ByteArrayOutputStream();
      byte[] buffer = new byte[4096];
      int n;
      while ((n = child.getInputStream().read(buffer)) != -1) output.write(buffer, 0, n);
      String text = output.toString("UTF-8");
      if (child.waitFor() != 1 || !text.contains(code) || text.contains("SYNTHETIC")
          || text.contains("Exception") || text.contains(file.toString()))
        throw new AssertionError("Process exit or redaction failed");
      checks++;
    } finally { Files.delete(file); }
  }
  public static void main(String[] args) throws Exception {
    JSONObject original = data();
    JSONObject parsed = CoreProvision.validatePayload(root(original), NOW);
    for (String key : new String[]{"account", "accountType", "timestamp", "signature", "type"}) {
      if (!original.getString(key).equals(parsed.getString(key))) throw new AssertionError("Changed value");
      checks++;
    }
    rejects("E_JSON", () -> CoreProvision.validatePayload("{", NOW));
    rejects("E_ADMIN", () -> CoreProvision.validatePayload(root(data()).replace("canary/", "other/"), NOW));
    rejects("E_SCHEMA", () -> CoreProvision.validatePayload(root(data().put("extra", "x")), NOW));
    JSONObject missing = data(); missing.remove("signature");
    rejects("E_SCHEMA", () -> CoreProvision.validatePayload(root(missing), NOW));
    rejects("E_SCHEMA", () -> CoreProvision.validatePayload(root(data().put("signature", 42)), NOW));
    rejects("E_SCHEMA", () -> CoreProvision.validatePayload(root(data().put("signature", " ")), NOW));
    rejects("E_PAIRING_TYPE", () -> CoreProvision.validatePayload(root(data().put("type", "batch")), NOW));
    rejects("E_TIMESTAMP", () -> CoreProvision.validatePayload(root(data().put("timestamp", "-1")), NOW));
    rejects("E_WINDOW", () -> CoreProvision.validatePayload(root(data().put("timestamp", "1799985599999")), NOW));
    rejects("E_WINDOW", () -> CoreProvision.validatePayload(root(data().put("timestamp", "1800000300001")), NOW));
    CoreProvision.requireLaunchSuccess(0); checks++;
    CoreProvision.requireUser(2000, 0); checks++;
    rejects("E_USER", () -> CoreProvision.requireUser(0, 0));
    rejects("E_USER", () -> CoreProvision.requireUser(2000, 10));
    for (int code : new int[]{-1, 1, 2, 3, 100, 101}) {
      rejects("E_LAUNCH_RESULT", () -> CoreProvision.requireLaunchSuccess(code));
    }
    if (CoreProvision.findLaunch(Overloads.class, new String[]{"java.lang.String"})
        .getParameterTypes()[0] != String.class) throw new AssertionError("Wrong overload");
    checks++;
    rejects("E_LAUNCH_API", () -> CoreProvision.findLaunch(Overloads.class, new String[]{"long"}));
    rejectsProcess("E_USAGE", "SYNTHETIC-PRIVATE", "invalid");
    rejectsProcess("E_JSON", "{SYNTHETIC-PRIVATE", "check");
    rejectsProcess("E_SCHEMA", root(data().put("signature", 42)), "check");
    rejectsProcess("E_SIZE", new String(new char[65537]).replace('\0', 'x'), "check");
    System.out.println("PASS: " + checks + " host assertions; no Android runtime or phone exercised.");
  }
}
