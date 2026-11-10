# Reading Python: what the parts do

Read a few lines at a time. Ask: **What data is here? What executes next? What repeats? What can change outside the program?** Predict before running. You do not need to memorize every library. You do need to check the important behavior before approving or using a script.

## Variables, assignment, and types

```python
server = "lab-web-01"
used_percent = 84
warning_at = 80
needs_review = used_percent >= warning_at
```

`server` is a name bound to a string, which is text. `used_percent` and `warning_at` refer to integers. `=` assigns a value. The comparison `>=` produces a boolean, True or False. The variable name is chosen by the programmer; it is not a Python keyword. Trace a name's value where it is assigned or updated.

`"84"` is text and `84` is a number. `input()` returns text. `int(text)` attempts conversion and can raise ValueError. `==` compares values, while `=` assigns. `in` checks membership: for strings, it checks whether one string occurs inside another. That makes `"active" in "inactive"` a useful review counterexample.

## Decisions, blocks, and indentation

```python
if used_percent >= warning_at:
    print("Review disk usage")
else:
    print("Below this warning threshold")
print("Check finished")
```

The colon begins a block. Four spaces is the usual indentation convention. Only the indented print under the selected branch runs. The final unindented print runs after either branch. A policy threshold is a decision rule for this exercise, not a universal rule for every server. Test the exact boundary, one below, and one above it.

## Lists, dictionaries, and indexing

```python
services = ["sshd.service", "crond.service"]
result = {"unit": "sshd.service", "returncode": 0}
print(services[0])
print(result["returncode"])
```

A list groups values in order. The first index is 0. A dictionary maps keys to values. `services[0]` selects by position; `result["returncode"]` selects by key. Brackets can mean list creation or a lookup depending on where they appear. Parentheses after a callable name mean a function call.

## For loops: one pass per item

```python
for service in services:
    print(service)
print("Finished")
```

The loop assigns the next item to `service`, executes the indented body, and continues until there are no items left. `service` is a programmer-chosen name, not a reserved word. The outer list `services` stays unchanged here. An empty list executes the body zero times. A three-item list executes it three times. `range(3)` supplies 0, 1, 2; the end value is excluded.

Trace table:

| Pass | service before print | Printed output |
| --- | --- | --- |
| 1 | first list item | first name |
| 2 | second list item | second name |
| After loop | last assigned item, if there was one | Finished |

Never assume an item variable exists after a loop over an empty collection. Avoid changing the list you are iterating unless you understand the effect.

## While loops: repeat while a condition stays true

```python
attempt = 0
while attempt < 3:
    print(attempt)
    attempt = attempt + 1
```

The condition is checked **before each pass**. Values printed are 0, 1, 2. At attempt 3, the condition is false and the loop ends. If the update is removed, this example never reaches its stopping value. Trace that failure on paper; do not run an infinite loop to prove it. Ctrl+C usually interrupts a terminal program.

`break` leaves the nearest enclosing loop. `continue` skips the rest of the current pass. A continue placed before a while-loop counter update can accidentally prevent progress. `for` is usually clearer when you already have a finite collection. `while` fits repetition governed by a changing condition, but requires a deliberate stopping argument. Real retry scripts also need limits and delays; this unit uses bounded printed examples rather than polling a server.

## Functions, arguments, return values, and side effects

```python
def label(name):
    return f"Report for {name}"

message = label("lab-web-01")
print(message)
```

`def` defines a function. Its body runs when called, not just because Python reads the definition. `name` is a parameter; `"lab-web-01"` is an argument. `return` sends a value to the caller. `print` displays output and returns None. A function with no explicit return also returns None. A function can also change a list, write a file, or start a process. Those are side effects, and a reviewer should identify them.

Read a call by locating the definition, identifying its inputs, following branches, and finding the return. You can understand a contract before studying every implementation detail.

## Imports: using another module

```python
import json
from pathlib import Path
```

`import json` loads the module and binds its name so `json.dumps(...)` is available. `from pathlib import Path` binds that specific name, so you can call `Path(...)`. Imports do not install packages. These two modules ship with Python's standard library. A local `import helper` can load helper.py; third-party modules may require a separate approved installation.

Importing a module executes its top-level initialization code the first time it loads in a process. An import is not a promise that no work will happen. Check unfamiliar modules and avoid naming your files `json.py` or `subprocess.py`, which can shadow standard-library modules.

```python
if __name__ == "__main__":
    main()
```

This common guard calls main when the file runs as a script. It avoids calling main merely because tests import the file. Other top-level code can still run on import. `main` itself is an ordinary function name chosen by the author.

## Exceptions and external results

An exception is a signaled Python error, such as missing files or timeouts. An external command can instead finish and return a nonzero **exit code** without raising an exception when check=False. These are different paths. Read specific except blocks and check whether they hide uncertainty or preserve it in the report.

## AI-assisted reading and review

Ask an assistant to explain a short region, identify assumptions, and propose test cases. Then independently trace a counterexample. If you cannot explain a change's purpose, inputs, outcome, and side effects, request a smaller change or more evidence before approval. Use documentation for unfamiliar options. You can look up details; you should not approve behavior you cannot evaluate.

Efficiency starts with unnecessary work you can count: repeated subprocess calls, repeated file reads, or nested scans. A shorter comprehension is not automatically clearer or faster. Count calls, test unchanged outputs, and use timings carefully when needed. Network and process overhead can dominate tiny syntax changes.
