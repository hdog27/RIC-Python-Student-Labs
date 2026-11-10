# Day 1: Why Python and Reading Code

Slide transcript. Follow the matching lesson from Start Here.

## Slide 1: Python in Linux admin work

Day 1
Reading, reviewing, and explaining code

## Slide 2: Where Python helps

| Role or task | Useful script behavior |
| --- | --- |
| Linux administration | Summarize service checks |
| Support and operations | Collect evidence for a ticket |
| Infrastructure automation | Apply consistent checks |

Discuss or try: Which repetitive task would you want to review or automate?

## Slide 3: Reviewing an AI draft

The author proposes behavior.
The reviewer checks intent and assumptions.
Tests supply evidence for a decision.

Discuss or try: What would you need to know before approving a script?

## Slide 4: Variables and values

```text
server = "lab-web-01"
used_percent = 84
warning_at = 80
needs_review = used_percent >= warning_at
```

Discuss or try: Name each variable, its type, and its current value.

## Slide 5: Assignment and comparison

| Python | What it does |
| --- | --- |
| used = 84 | Assign a value |
| used == 84 | Compare for equality |
| used >= 80 | Compare with a threshold |
| "84" | Text, rather than a number |

Discuss or try: What changes if the input is text?

## Slide 6: Decisions and indentation

```text
if used_percent >= warning_at:
    print("Review disk usage")
else:
    print("Below this threshold")
print("Check finished")
```

Discuss or try: Which print belongs to a branch? Which always runs afterward?

## Slide 7: A service-report record

```text
result = {
    "unit": "sshd.service",
    "returncode": 0,
    "stdout": "active",
    "stderr": "",
    "error": ""
}
```

Discuss or try: What can you infer? What would still need checking?

## Slide 8: Reading before running

Purpose and inputs.
Next line, branch, and return.
Actions outside the program.

Discuss or try: Which facts can you trace, and which need documentation?

## Slide 9: Today’s investigation

Trace the variable example.
Test one below, at, and above a threshold.
Annotate a short region of the supplied app.

Discuss or try: Follow Day 1 from Start Here and save the baseline tests.

## Slide 10: The review checkpoint

You can explain a value and predict a branch.

Discuss or try: What evidence would change your decision about this script?

Concept references:
https://docs.python.org/3/tutorial/introduction.html
https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/htmlsingle/configuring_basic_system_settings/index
