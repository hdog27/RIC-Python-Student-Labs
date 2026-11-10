# Day 3: Saving data safely

Student-readable slide transcript. Full lab instructions are in the matching daily lab.

## Slide 1: Saving data safely

Day 3
Tasks that survive a restart

---

## Slide 2: Today’s build

Load valid data at startup.
Save after a change.
Keep damaged data available for recovery.

**Discuss or try:** What evidence proves that a restart worked?

---

## Slide 3: The data journey

1. Python task list
2. JSON text file
3. Validated task list

**Discuss or try:** Which step can fail? What should the app preserve?

---

## Slide 4: JSON and Python

| Meaning | Python | JSON |
| --- | --- | --- |
| Boolean | False | false |
| Collection | list | array |
| Record | dict | object |

**Discuss or try:** Does valid JSON always match our task contract?

---

## Slide 5: A small round-trip

```python
import json

original = {"read": False}
text = json.dumps(original)
restored = json.loads(text)
print(restored == original)
```

**Discuss or try:** What is the type of text? What is the type of restored?

---

## Slide 6: Different failures

| Situation | Response |
| --- | --- |
| File is missing | Start a new empty tracker |
| JSON or schema is invalid | Report and preserve the file |
| File access fails | Report the access problem |

**Discuss or try:** Why could an empty fallback cause data loss?

---

## Slide 7: A specific exception

```python
try:
    minutes = int(input("Minutes: "))
except ValueError:
    print("Enter a whole number")
```

**Discuss or try:** Which error can this code handle? Which errors remain?

---

## Slide 8: Lab: JSON investigation

Round-trip a small record.
Compare missing, malformed, and wrong-schema files.
Keep the original bytes unchanged.

**Discuss or try:** Use scratch copies of the supplied fixtures.

---

## Slide 9: Project checkpoint

validate_tasks
load_tasks
save_tasks

**Discuss or try:** Add a task, quit, restart, and verify the same data.

---

## Slide 10: Before you leave

Parsing checks syntax. Validation checks the data contract.

**Discuss or try:** Why should a failed load prevent normal saving?

---

Concept reference: https://docs.python.org/3.11/library/json.html
