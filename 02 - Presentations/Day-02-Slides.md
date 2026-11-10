# Day 2: For and While Loops

Slide transcript. Follow the matching lesson from Start Here.

## Slide 1: For and while loops

Day 2
What repeats, and what makes it stop?

## Slide 2: A list of services

```text
services = [
    "sshd.service",
    "crond.service",
    "httpd.service",
]
print(services[0])
```

Discuss or try: What is the first position? What if the list is empty?

## Slide 3: For: one pass per item

```text
for service in services:
    print(service)
print("Finished")
```

Discuss or try: Mark the repeated block and the first line after it.

## Slide 4: A for-loop trace

| Pass | service value | Body executions so far |
| --- | --- | --- |
| 1 | sshd.service | 1 |
| 2 | crond.service | 2 |
| 3 | httpd.service | 3 |

Discuss or try: Which value changes each pass? Does the list change here?

## Slide 5: While: check before each pass

```text
attempt = 0
while attempt < 3:
    print(attempt)
    attempt = attempt + 1
```

Discuss or try: Trace the condition, body, and update in that order.

## Slide 6: The stopping argument

| Before condition | attempt < 3 | Next action |
| --- | --- | --- |
| 0 | True | Print, then update |
| 1 | True | Print, then update |
| 2 | True | Print, then update |
| 3 | False | Leave the loop |

Discuss or try: What if the update disappears?

## Slide 7: Break and continue

break leaves the nearest loop.
continue skips to the next pass.
A skipped counter update can prevent progress.

Discuss or try: Where must the update occur in a bounded while loop?

## Slide 8: Loops in the supplied app

main queries each configured service.
build_report turns each result into one row.

Discuss or try: Count queries and report rows separately.

## Slide 9: Today’s investigation

Trace zero, one, and three passes.
Repair the bounded-loop draft.
Explain which loop fits a known list.

Discuss or try: Use the Day 2 lesson and workbook trace table.

## Slide 10: The review checkpoint

You can identify repetition and justify termination.

Discuss or try: What value changes so your while loop can stop?

Concept references:
https://docs.python.org/3/tutorial/controlflow.html
https://docs.python.org/3/tutorial/introduction.html
