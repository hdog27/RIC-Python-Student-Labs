# Day 3: Imports and RHEL Commands

Slide transcript. Follow the matching lesson from Start Here.

## Slide 1: Imports and RHEL commands

Day 3
How a Python script uses existing tools

## Slide 2: Imports make names available

```text
import json
from pathlib import Path
import subprocess
```

Discuss or try: Which name do you use to call each library?

## Slide 3: Definitions and calls

```text
def label(name):
    return f"Report for {name}"

message = label("lab-web-01")
print(message)
```

Discuss or try: When does the body execute? Where does the result go?

## Slide 4: The terminal command

```text
systemctl is-active sshd.service
```

Discuss or try: What is the executable? Which parts are arguments?

## Slide 5: The Python process call

```text
result = subprocess.run(
    ["systemctl", "is-active", "sshd.service"],
    capture_output=True,
    text=True,
    timeout=5,
    check=False,
)
```

Discuss or try: Explain one option before the instructor runs it.

## Slide 6: The returned evidence

| Field | What to inspect |
| --- | --- |
| stdout | Normal output, such as active |
| stderr | Diagnostic text, possibly empty |
| returncode | Command-specific completion status |

Discuss or try: Can a nonzero status be an expected service-state result?

## Slide 7: A report preserves uncertainty

| Observed evidence | Classroom label |
| --- | --- |
| Code 0 and exact active | ok |
| Nonzero and inactive or failed | attention |
| Missing, conflicting, or uncertain | unknown |

Discuss or try: Does active alone prove the application serves users?

## Slide 8: RHEL inspection tools

| Question | Read-only command |
| --- | --- |
| Which account? | whoami |
| Disk usage? | df -h / |
| Service state? | systemctl is-active sshd.service |
| Recent visible logs? | journalctl -u sshd.service -n 10 --no-pager |

Discuss or try: Why might the visible journal be incomplete?

## Slide 9: Today’s investigation

Annotate imports and query_service.
Translate one command into an argument list.
Compare result fields and error paths.

Discuss or try: Use simulated results or the assigned RHEL VM, and say which.

## Slide 10: The review checkpoint

You can explain what ran and what its result means.

Discuss or try: How is a command’s nonzero code different from a Python exception?

Concept references:
https://docs.python.org/3/tutorial/modules.html
https://docs.python.org/3/library/subprocess.html
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/htmlsingle/configuring_basic_system_settings/index
