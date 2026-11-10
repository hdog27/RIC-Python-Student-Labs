# Day 1: First Python program

Student-readable slide transcript. Full lab instructions are in the matching daily lab.

## Slide 1: Your first Python program

Day 1
TaskTrack: a five-day Python project

---

## Slide 2: Today’s build

A program that collects input and makes a decision.

By the end: a task-entry prototype and a user story.

**Discuss or try:** Who would use your tracker?

---

## Slide 3: Predict the output

```python
print("3" + "4")
print(3 + 4)
```

**Discuss or try:** What changes when the quotes disappear?

---

## Slide 4: Names and values

```python
minutes = 12
sessions = 3
total = minutes * sessions
print(total)
```

**Discuss or try:** Which line changes a value? Which line displays it?

---

## Slide 5: Input and types

| Expression | Kind of value |
| --- | --- |
| input("Minutes: ") | str |
| int("12") | int |
| 12 > 0 | bool |

**Discuss or try:** Which operation needs numeric input?

---

## Slide 6: A decision in code

```python
minutes = int(input("Minutes: "))
if minutes > 0:
    print("Ready to plan")
else:
    print("Choose a positive value")
```

**Discuss or try:** Try 12, 0, and -3. Predict each branch first.

---

## Slide 7: An experiment that fails

```python
minutes = input("Minutes: ")
print(minutes + 5)
```

**Discuss or try:** State the types. What did the programmer intend?

---

## Slide 8: Lab: session estimator

Ask for an activity and minutes.
Calculate three sessions.
Handle zero and negative durations.

**Discuss or try:** Record predicted and actual results for four inputs.

---

## Slide 9: Project checkpoint

A fictional user and a clear need.
A title-entry prototype.
A sketch of add, list, complete, and quit.

**Discuss or try:** Show your prototype to a partner before extending it.

---

## Slide 10: Before you leave

You can read input, convert a value, and choose a branch.

**Discuss or try:** Why does input need conversion before numeric addition?

---

Concept reference: https://docs.python.org/3.11/tutorial/introduction.html
