# Day 2: Data and functions

Student-readable slide transcript. Full lab instructions are in the matching daily lab.

## Slide 1: Data and functions

Day 2
A tracker with several tasks

---

## Slide 2: Today’s build

A list of task records.
Functions that add, list, and complete tasks.

**Discuss or try:** What information belongs in one task record?

---

## Slide 3: ID and position

| List position | Stable ID | Title |
| --- | --- | --- |
| 0 | 1 | Read |
| 1 | 7 | Practice |

**Discuss or try:** Which task does tasks[1] select? Which ID does it have?

---

## Slide 4: One record

```python
task = {
    "id": 7,
    "title": "Practice",
    "done": False
}
print(task["title"])
```

**Discuss or try:** What would task["done"] return?

---

## Slide 5: A loop over records

```python
books = [{"pages": 12}, {"pages": 8}]
for book in books:
    print(book["pages"])
```

**Discuss or try:** Trace the loop once per dictionary.

---

## Slide 6: A returned result

```python
def double(number):
    return number * 2

answer = double(6)
print(answer)
```

**Discuss or try:** How would the caller use a printed value instead?

---

## Slide 7: Function contracts

Inputs: what the caller supplies.
Result: what the function returns.
Side effects: what it changes.

**Discuss or try:** Describe a contract before writing its implementation.

---

## Slide 8: Lab: equipment checkout

Model equipment as records.
Return available names.
Check out an item by stable ID.

**Discuss or try:** Test IDs 1, 7, and 99. Include an empty list.

---

## Slide 9: Project checkpoint

add_task
list_tasks
complete_task

**Discuss or try:** Demonstrate in-memory behavior using IDs with a gap.

---

## Slide 10: Before you leave

A function can return a value and change existing data.

**Discuss or try:** Why should task IDs survive a change in list position?

---

Concept reference: https://docs.python.org/3.11/tutorial/datastructures.html
