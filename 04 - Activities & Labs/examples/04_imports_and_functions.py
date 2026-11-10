import json
from pathlib import Path

def describe(name):
    return f"Report for {name}"

if __name__ == "__main__":
    record = {"message": describe("lab-web-01")}
    print(json.dumps(record))
    print(Path("report.json").name)
