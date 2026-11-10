# Python reference sheet

| Concept | Small example | Watch for |
| --- | --- | --- |
| Assignment | `minutes = 15` | `=` stores a value |
| Comparison | `minutes == 15` | `==` compares values |
| String input | `name = input("Name: ")` | Input returns text |
| Conversion | `count = int("3")` | Non-numeric text raises ValueError |
| Formatting | `print(f"Hello {name}")` | Prefix the string with `f` |
| Boolean | `finished = False` | Python uses True/False |
| Branch | `if count > 0:` | Indent the body four spaces |
| List | `items = ["pen", "book"]` | Index 0 is the first item |
| Dictionary | `item = {"name": "pen"}` | Access with `item["name"]` |
| Loop | `for item in items:` | The body runs for each item |
| Function | `def double(n): return n * 2` | Return passes a result to the caller |
| Import | `from pathlib import Path` | Use standard-library modules |
| Exception | `except ValueError:` | Catch the error you can handle |
| JSON | `json.dumps({"name": "pen"})` | JSON text differs from Python syntax |
| Test | `self.assertEqual(double(4), 8)` | Check observable behavior |

```python
def double(n):
    return n * 2

for value in [2, 4, 6]:
    print(double(value))
```

Traceback routine: read the last line, locate your file and line, state what you expected, reproduce with the smallest input, change one thing, rerun. Keep the full error text in your debugging log.

Function contract routine: write the inputs, returned value, side effects, invalid inputs, and one concrete example before coding. A function can change a list even if it returns nothing. Distinguish the returned value from the printed output.

Common commands from your app folder:

```text
python app.py
python -m unittest -v
python -m py_compile app.py tracker.py test_tracker.py
```

Use the Python command selected during setup. See the annotated resources for official explanations and practice targets.
