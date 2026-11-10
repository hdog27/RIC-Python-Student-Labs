# Day 4: AI Review and Efficiency

Slide transcript. Follow the matching lesson from Start Here.

## Slide 1: AI review and efficiency

Day 4
A decision supported by counterexamples

## Slide 2: An approval decision

Intent: what should happen?
Trace: what actually happens?
Evidence: why accept, edit, or reject?

Discuss or try: Which assumption would you test first?

## Slide 3: A plausible-looking mistake

```text
state = "inactive"
if "active" in state:
    print("healthy")
```

Discuss or try: Predict the output. Is membership the intended comparison?

## Slide 4: A claim about repetition

```text
attempt = 0
while attempt < 3:
    print("Checking again")
```

Discuss or try: Trace four imagined passes without running this draft.

## Slide 5: Repeated external work

```text
for unit in services:
    print(unit, read_state(unit), read_state(unit))
```

Discuss or try: For two services, how many child commands could this start?

## Slide 6: One observation reused

```text
for unit in services:
    state = read_state(unit)
    print(unit, state, state)
```

Discuss or try: What behavior must your test preserve?

## Slide 7: Efficiency evidence

| Version | Queries for two services |
| --- | --- |
| Repeated-read draft | 4 |
| Reuse one result | 2 |

Discuss or try: Why is a shorter source file weak evidence of improvement?

## Slide 8: Useful counterexamples

Inactive contains the letters active.
An empty list makes zero passes.
A timeout gives no reliable service state.

Discuss or try: Which test can disprove the draft’s strongest claim?

## Slide 9: Today’s investigation

Review all three drafts.
Test small repairs.
Count unnecessary work before and after.

Discuss or try: Log one suggestion you accepted, edited, or rejected.

## Slide 10: The review checkpoint

Approval includes a reason, evidence, and known limits.

Discuss or try: What did your tests establish, and what remains uncertain?

Concept references:
https://docs.python.org/3/library/subprocess.html
https://docs.python.org/3/library/unittest.html#basic-example
