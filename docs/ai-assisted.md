# Easier option: let a local AI assistant handle the computer work

**Claude Code, Kimi Code, or Codex can make this much easier:** the assistant can run commands, inspect errors and follow this guide while you handle physical phone prompts. You do not need to be a coder.

It needs **local computer access on the machine connected to the phone**. A normal browser chat or cloud-only coding session cannot automatically see your USB phone. The assistant must check its tools and explain missing access. AI can make mistakes; the guide's verification steps still apply.

## 1. Download the guide

Click [Download guide ZIP](https://github.com/bokiko/acurast-core-onboarding-guide/archive/refs/heads/main.zip). In Downloads, extract it so **acurast-core-onboarding-guide-main** contains `AI-ONBOARDING.md`, `README.md`, `docs` and `tools`. Do not work inside a ZIP preview.

Already have a local AI app? Open it, select this extracted folder as its local project/workspace, then skip to step 3. Explicitly naming the instruction file works even if the app does not automatically load repository instructions.

## 2. Install one assistant if needed

Choose **one**, not all three. Each service has its own sign-in, availability and usage terms; this guide does not promise free access. These official installer commands were checked on 2026-09-09. They download and run installer code from the named vendor.

**Where commands go:** Mac: Command+Space → Terminal → Enter. Windows: Start → PowerShell → Windows PowerShell. Ubuntu: Ctrl+Alt+T. Expand your chosen assistant, copy the box for your computer, paste into that window and press Enter.

<details>
<summary><strong>Install Claude Code</strong></summary>

Mac / Linux Terminal:

```sh
curl -fsSL https://claude.ai/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://claude.ai/install.ps1 | iex
```

</details>

<details>
<summary><strong>Install Kimi Code</strong></summary>

Mac / Linux Terminal:

```sh
curl -fsSL https://code.kimi.com/kimi-code/install.sh | bash
```

Windows PowerShell:

```powershell
irm https://code.kimi.com/kimi-code/install.ps1 | iex
```

</details>

<details>
<summary><strong>Install Codex</strong></summary>

Mac / Linux Terminal:

```sh
curl -fsSL https://chatgpt.com/codex/install.sh | sh
```

Windows PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

</details>

Close and reopen the terminal afterward. Enter the guide folder:

**Mac / Ubuntu:**

```sh
cd "$HOME/Downloads/acurast-core-onboarding-guide-main"
```

**Windows PowerShell:**

```powershell
Set-Location "$HOME\Downloads\acurast-core-onboarding-guide-main"
```

Type **only the name you installed**—`claude`, `kimi`, or `codex`—and press Enter. The assistant opens in the terminal. Follow its sign-in prompts in the browser. Codex offers **Sign in with ChatGPT**; Claude prompts for account sign-in. For Kimi, if needed type `/login` in its conversation and follow its provider/account prompts. Enter credentials only in the vendor's sign-in flow.

If the command is missing, reopen the terminal and retry. If install/login fails, keep its exact error; do not paste API keys into the repository or disable all approval controls. You can use the manual walkthrough instead.

Optional official references: [Claude Code](https://code.claude.com/docs/en/overview), [Kimi Code](https://moonshotai.github.io/kimi-code/), [Codex CLI](https://developers.openai.com/codex/cli/).

## 3. Paste this into the assistant's conversation

**This text goes in the AI chat input, not a normal shell prompt.** Read the authorization paragraph; remove anything you do not authorize. Do not claim a backup exists if it does not.

```text
Read AI-ONBOARDING.md in this guide folder, then read the guide pages it names.
Help me onboard my own dedicated Android phone to Acurast Core, not Lite.
I am not a coder: do the computer work where your tools allow, explain progress simply,
and tell me exactly what to tap when a physical action is needed.

Start with read-only checks of this computer and the attached phone. Confirm the correct
phone and whether it is backed up before changing it. Once I confirm the target and backup,
I authorize the documented Core setup: verified download/install, required blocker settings,
removing setup accounts from this phone after explaining the local-data effects, device-owner
registration, and pairing with my own fresh Hub data. Check each result before moving on.

Ask me separately before any factory reset, firmware flash, bootloader change, data wipe,
or replacement of an already-paired processor. Do not ask for passwords or wallet recovery
words in chat. Keep QR data in a private local file, not in chat or public logs.
If you cannot access this computer's USB device, say so and guide me through the manual steps.
Do not claim success until the intended processor is confirmed online in my Hub.
```

The assistant should check its actual tools and device access first. It may need your permission for local commands. Approve only actions you understand and intend; this guide does not require turning off all approvals.

## 4. Your part while the assistant works

- Connect the intended phone with a data cable and unlock it.
- Accept the phone's USB-debugging authorization when asked.
- Handle SIM insertion, passwords, vendor sign-in and physical confirmations yourself.
- Create fresh QR data in your own Hub when asked. Use [the private save instructions](start-here.md#8-get-and-save-your-qr-data); tell the assistant the file location rather than pasting JSON into chat.
- Read and accept any legal disclaimer yourself if you agree.
- Confirm online status under the intended Hub wallet if the assistant cannot inspect that browser session.

## 5. If it gets stuck

Say: **“Stop repeating the failed command. Read the troubleshooting section, tell me the last successful step and the exact blocker, and give me one concrete next action.”**

If switching assistants, request a short handoff with model, Android/Core version, last successful stage and next action—without secrets. The new assistant must recheck the connected phone. Never run two assistants changing the same phone at once.

**The file to give any assistant is [AI-ONBOARDING.md](../AI-ONBOARDING.md).** It is plain text; no plugin is needed. `AGENTS.md` and `CLAUDE.md` also point to it for tools that recognize those files. They do not start phone work automatically.

Prefer manual setup? [The beginner walkthrough](start-here.md) includes downloads, phone menus, commands, expected results and fixes on one page.
