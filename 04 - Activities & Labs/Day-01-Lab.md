# Day 1: First Python program

**Learning target:** Collect a fictional task title and a positive estimated duration. Display a readable summary. Explain why input needs conversion.

**You need:** your editor, Python, a writable project folder, and today's workbook page. The guided lab takes 50 minutes plus a 15-minute share-out. Project work takes a separate 180 minutes. Pairing is encouraged; change driver every 15 minutes.

## Predict before running

What does `print("3" + "4")` display? What changes if both values pass through `int()`?

Write your prediction and the reason. Run a small experiment to check it.

## Guided lab: Build a session estimator

1. Create `day1_estimator.py`. Ask for a fictional activity and minutes per session.
2. Predict the type of both input values. Print their types once to check your prediction.
3. Convert minutes to an integer. Compute the minutes for three sessions.
4. Use an if/else decision to show a useful message when minutes is positive or non-positive. For today, assume numeric input. Record what happens for letters so Day 3 can fix it.
5. Test 12, 1, 0, and -3. Write predicted and actual results. Explain why "12" and 12 behave differently.
6. Ask a partner to try it. Improve one prompt based on their feedback.

## Project work

Write a user story for TaskTrack. In `day1_prototype.py`, ask for a title, reject whitespace-only titles using `.strip()`, and print a task summary. Sketch add/list/complete/quit on paper. Do not build persistence yet.

Work in three 60-minute blocks: build the core milestone, test it with a peer, then improve and document it. Before adding an extension, demonstrate the required milestone to your instructor.

## Checkpoint and submission

Submit estimator code, four numeric test cases, a recorded non-numeric failure, a task-entry prototype, and a user story. Include exact commands and inputs so someone else can repeat your result. A screenshot helps but does not replace your source files.

## Exit ticket

Explain the difference between assignment and comparison. Why can input("Minutes: ") not be added directly to 5?

## Need a hint?

State the smallest input that fails. Locate the matching concept in the Python reference sheet. Write the expected result before asking for a code suggestion. Ask your instructor for a targeted hint if you remain stuck after ten minutes.

## Extension

Add a configurable session count and a second boundary check. Explain the behavior for zero sessions.
