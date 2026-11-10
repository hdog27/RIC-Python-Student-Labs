# Day 4: Debugging and tests

Student-readable slide transcript. Full lab instructions are in the matching daily lab.

## Slide 1: Debugging and tests

Day 4
Evidence for a working app

---

## Slide 2: Today’s build

A complete menu flow.
Repeatable tests.
A debugging log someone else can reproduce.

**Discuss or try:** What does “it works” need as evidence?

---

## Slide 3: A useful test case

| Part | Example |
| --- | --- |
| Setup | Empty task list |
| Action | Add a whitespace-only title |
| Expected | ValueError, list unchanged |

**Discuss or try:** What would a vague “test bad input” miss?

---

## Slide 4: An automated check

```python
import unittest

class DoubleTests(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(double(0), 0)
```

**Discuss or try:** If this passes, have we proved double always works?

---

## Slide 5: Reading a failure

Expected: 0
Actual: 1
Smallest input: an empty list

**Discuss or try:** Which hypothesis could explain the extra one?

---

## Slide 6: Cases worth checking

| Category | Example |
| --- | --- |
| Boundary | No tasks |
| Invalid input | Unknown ID |
| Persistence | Save, restart, load |
| Regression | A previously failing input |

**Discuss or try:** Which case can expose a defect that a normal example misses?

---

## Slide 7: A debugging record

Exact command and input.
Expected and actual result.
Hypothesis, change, and retest.

**Discuss or try:** Can your partner reproduce the problem from your notes?

---

## Slide 8: Lab: broken summary

Predict before execution.
Find the smallest failure.
Keep a regression case after the repair.

**Discuss or try:** Add all-complete and none-complete cases.

---

## Slide 9: Project checkpoint

All supplied acceptance checks.
Four original tests.
The manual CLI checklist.

**Discuss or try:** Check both core functions and the user’s menu flow.

---

## Slide 10: Before you leave

Tests make a claim repeatable. They cover the cases you chose.

**Discuss or try:** Which bug would your newest test catch?

---

Concept reference: https://docs.python.org/3.11/library/unittest.html#basic-example
