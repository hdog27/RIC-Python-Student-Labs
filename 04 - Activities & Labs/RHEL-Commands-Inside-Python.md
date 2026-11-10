# RHEL commands inside Python

## Why a Linux administrator would use Python

A terminal command answers one question. Python can apply the same question to several approved services, make decisions using the results, retain errors, and produce a structured report for a support ticket. Examples include a daily service check, a disk-capacity summary, or a report comparing configuration observations. The administrator still needs to judge whether the script's assumptions match the server.

Bash is often convenient for a short command sequence or pipeline. Python becomes useful when the job needs structured records, reusable functions, parsing, tests, or several error paths. Use the tool that keeps the work understandable. Knowing Python helps you review automation even when an AI assistant produces the first draft. This unit makes no prediction that all future jobs will use the same tools.

## 1. Read the command before wrapping it

Run these manually only on the instructor-assigned RHEL 9 or compatible lab VM. All commands below inspect state; none starts/stops services, installs packages, or changes configuration. Commands execute on the machine running Python. They do not automatically connect to a remote host.

| Command | What it asks | What to watch for |
| --- | --- | --- |
| `whoami` | Which account runs this process? | Script permissions follow that account |
| `df -h /` | Show human-readable usage for the filesystem containing / | Human-readable text is for inspection, not our parsing contract |
| `free -m` | Show memory figures in mebibytes on the lab's procps implementation | Available memory differs from unused/free memory |
| `systemctl is-active sshd.service` | What is the service's active state? | Inspect both output and exit code |
| `systemctl is-enabled sshd.service` | Is the unit enabled/configured for activation? | Enabled is distinct from currently running |
| `systemctl status sshd.service --no-pager` | Show detailed status for a person to inspect | Output can include timestamps/logs and a nonzero status |
| `journalctl -u sshd.service -n 10 --no-pager` | Show up to ten available journal entries for that unit | Your account may see only some entries, or none |

The service names are examples, not a guarantee that every VM installs them. An absent httpd.service is a valid observation, not an instruction to install Apache. If a log command lacks permission, record the limitation and use the fictional sample. Do not add sudo just to make an exercise appear successful.

RHEL documentation: [basic system settings, service and log inspection](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/htmlsingle/configuring_basic_system_settings/index). Local `man systemctl`, `man journalctl`, `man df`, and `man free` describe the exact versions on the assigned VM.

## 2. Translate a command into arguments

Terminal:

```text
systemctl is-active sshd.service
```

Python:

```python
import subprocess

result = subprocess.run(
    ["systemctl", "is-active", "sshd.service"],
    capture_output=True,
    text=True,
    timeout=5,
    check=False,
)
print(result.stdout.strip())
print(result.returncode)
print(result.stderr.strip())
```

| Part | Meaning |
| --- | --- |
| `import subprocess` | Make Python's process-running library available |
| `subprocess.run(...)` | Start a child process and wait for it to finish |
| First list item | Executable name, located using the process environment's PATH |
| Remaining list items | Separate arguments, just as the command expects |
| `capture_output=True` | Keep stdout and stderr so Python can inspect them |
| `text=True` | Decode captured output as strings rather than bytes |
| `timeout=5` | Limit the waiting time; TimeoutExpired is a separate error path |
| `check=False` | Return nonzero exit codes for our code to interpret |
| `result.stdout` | The command's normal output |
| `result.stderr` | Its error/diagnostic output, which may be empty even for nonzero exits |
| `result.returncode` | Integer exit status; interpret it using that command's documented meaning |

No shell is requested here: shell=False is the default. Python passes a list of arguments rather than a command string for a shell to interpret. Pipes, redirects, `&&`, and `$HOME` are not interpreted as shell syntax in that list. Do not append them and expect terminal behavior. `cd` is a shell builtin; use subprocess's cwd argument for a child's directory or pathlib for file paths. A child process cannot change your parent terminal's directory.

Using an argument list avoids shell interpretation, but it does not make every possible executable or argument harmless. The teaching app restricts service names and the verb. Changing the arguments to restart, delete, or install changes the action. Review what the command actually does.

## 3. Interpret a finished command

For **one unit** queried with systemctl is-active, active state normally returns 0. A non-active state returns nonzero. A missing/unknown unit or a broken systemd environment also needs interpretation. A nonzero code alone does not prove a command failed to launch. A timeout or missing executable is a Python exception instead.

Our classroom reporting policy is deliberately explicit:

| Evidence | Report label |
| --- | --- |
| Code 0 and exact state active, no command exception | ok |
| Nonzero code and exact state inactive or failed, no command exception | attention |
| Missing command, timeout, missing/unknown unit, unexpected state, or contradictory fields | unknown |

These are reporting decisions, not a universal health-monitoring standard. Active does not prove an application serves requests correctly. Successful report creation (the Python script's exit 0) does not mean every inspected service is healthy. The report retains each command's exit code and uncertainty.

## 4. Read the supplied wrapper

Open `05 - Final Project/serverbrief/serverbrief.py` from the repository root. In query_service, locate the allowlist, command list, timeout, exception paths, and returned record. Then find the for loop in main that invokes it once per configured service. Trace the result into build_report and classify. No network/API account is involved.

## 5. Compare sample mode and live mode

Sample mode works anywhere and launches no Linux commands:

```text
python serverbrief.py
```

Inside your copied app folder on the assigned RHEL VM, use that VM's interpreter:

```text
python3 --version
python3 serverbrief.py --live
```

The live script queries sshd.service and crond.service. It runs as your ordinary account and has a five-second timeout per query. A container or WSL environment without a usable systemd system bus is not equivalent to a full RHEL VM. Record unknown results honestly. Do not enable systemd or change the VM just for this script without instructor preparation.

The input sample additionally includes a fictional missing httpd.service. Compare only matching units when contrasting sample and live results. Retain the report's source label. If sharing live observations, redact host/user details and journal content. Fictional data is preferred for portfolios.

## 6. Save a report

```text
python serverbrief.py --output review-report.json
```

This creates a new local JSON file. Choose a new filename for later runs: the script intentionally refuses to overwrite an existing report. No server configuration changes. Use json rather than parsing human-oriented status tables for the final artifact.

Reference: [Python subprocess API](https://docs.python.org/3/library/subprocess.html). Read the options used above, not every advanced process-control API.
