"""ServerBrief: a supplied app to READ, REVIEW, TEST, and improve.

Default mode reads fictional saved command results. --live queries only the
fixed service names on the assigned Linux lab machine. No administrative changes.
"""
import argparse
import json
import platform
import subprocess
from pathlib import Path

SERVICES = ["sshd.service", "crond.service"]
ALLOWED_SERVICES = {"sshd.service", "crond.service", "httpd.service"}
SAMPLE = Path(__file__).resolve().with_name("sample-results.json")

def classify(result):
    """Classroom policy: command problems/uncertain results stay unknown."""
    state = result["stdout"].strip()
    code = result["returncode"]
    if result["error"]:
        return "unknown"
    if code == 0 and state == "active":
        return "ok"
    if code is not None and code != 0 and state in ("inactive", "failed"):
        return "attention"
    return "unknown"

def query_service(unit, runner=subprocess.run):
    """Return a record. runner is replaceable so tests need no real server."""
    if unit not in ALLOWED_SERVICES:
        raise ValueError("Choose a service in the classroom allowlist")
    command = ["systemctl", "is-active", unit]
    try:
        completed = runner(command, capture_output=True, text=True,
                           timeout=5, check=False)
    except subprocess.TimeoutExpired:
        return {"unit": unit, "returncode": None, "stdout": "",
                "stderr": "", "error": "command timed out"}
    except OSError as error:
        return {"unit": unit, "returncode": None, "stdout": "",
                "stderr": "", "error": str(error)}
    return {"unit": unit, "returncode": completed.returncode,
            "stdout": completed.stdout, "stderr": completed.stderr,
            "error": ""}

def load_sample(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Sample must contain a list of command-result records")
    for record in data:
        if not isinstance(record, dict) or set(record) != {
                "unit", "returncode", "stdout", "stderr", "error"}:
            raise ValueError("Each sample record needs the documented five fields")
        if not isinstance(record["unit"], str) or record["unit"] not in ALLOWED_SERVICES:
            raise ValueError("Sample contains an unapproved service name")
        if record["returncode"] is not None and type(record["returncode"]) is not int:
            raise ValueError("returncode must be an integer or null")
        if not all(isinstance(record[key], str) for key in ("stdout", "stderr", "error")):
            raise ValueError("Output and error fields must be strings")
    return data

def build_report(results, source):
    rows = []
    for result in results:
        rows.append({"unit": result["unit"], "status": classify(result),
                     "state": result["stdout"].strip(),
                     "returncode": result["returncode"],
                     "error": result["error"], "stderr": result["stderr"]})
    return {"source": source, "services": rows}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true", help="query assigned Linux lab VM")
    parser.add_argument("--output", type=Path, help="save JSON to a new file in your working folder")
    args = parser.parse_args()
    if args.live and platform.system() != "Linux":
        parser.error("Live mode needs the assigned Linux VM. Omit --live for sample mode.")
    try:
        if args.live:
            results = []
            for unit in SERVICES:
                results.append(query_service(unit))
            source = "live"
        else:
            results = load_sample(SAMPLE)
            source = "simulated"
        report = build_report(results, source)
        rendered = json.dumps(report, indent=2)
        print(rendered)
        if args.output:
            # Exclusive creation preserves any report already at this path.
            with args.output.open("x", encoding="utf-8") as output:
                output.write(rendered + "\n")
    except (OSError, ValueError) as error:
        parser.error(str(error))
    # Success here means report creation succeeded, not that every service is healthy.
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
