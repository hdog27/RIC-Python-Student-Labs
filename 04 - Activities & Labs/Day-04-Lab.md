# Day 4: Debugging and tests

**Learning target:** Use repeatable tests to diagnose defects and verify an integrated command-line workflow.

**You need:** your editor, Python, a writable project folder, and today's workbook page. The guided lab takes 50 minutes plus a 15-minute share-out. Project work takes a separate 180 minutes. Pairing is encouraged; change driver every 15 minutes.

## Predict before running

A program works for three tasks. Does that tell us what it does for zero tasks or an unknown ID?

Write your prediction and the reason. Run a small experiment to check it.

## Guided lab: Repair a broken function

1. Copy `broken_summary.py` into your workspace. Read it before running it.
2. Run its embedded tests. Record expected versus actual results for zero tasks and a mixture of open and completed tasks.
3. State a hypothesis about the defect. Change one line at a time and rerun the failing test.
4. Add a new case where every task is complete and another where none is complete. Keep these regression tests.
5. Open the test_tracker.py file in your app folder. Run one named test, then the full suite.
6. Ask a partner to explain a failure message without looking at your implementation. Decide whether the error belongs to the code, the test, or the documented requirement.

## Project work

Finish the CLI integration and add at least four original tests beyond the supplied acceptance suite. Include an edge case, invalid input, persistence, and a case tied to your chosen extension or a bug you found. Run the manual acceptance checklist with a partner. Keep a debugging log.

Work in three 60-minute blocks: build the core milestone, test it with a peer, then improve and document it. Before adding an extension, demonstrate the required milestone to your instructor.

## Checkpoint and submission

Submit fixed summary, regression cases, four original tests, full test output, and a debugging log with a reproduced defect. Include exact commands and inputs so someone else can repeat your result. A screenshot helps but does not replace your source files.

## Exit ticket

Why can a passing test suite still miss a bug? What makes a regression test useful?

## Need a hint?

State the smallest input that fails. Locate the matching concept in the Python reference sheet. Write the expected result before asking for a code suggestion. Ask your instructor for a targeted hint if you remain stuck after ten minutes.

## Extension

Write a subprocess smoke test that sends menu input to a temporary copy of the app and checks the saved file.
