# Day 2: For loops and while loops

Goal: **Trace what repeats, count executions, and justify how a loop ends.**

Vocabulary: lists, dictionary lookups, loop variables, iteration, range, conditions, counters, break and continue.

## Read first

Read these sections of the Python reading guide: Lists, dictionaries, and indexing; For loops; While loops. The guide is in `03 - Student Worksheets and Packet`. Today's example is `02_for_loop.py and 03_while_loop.py`. Short examples are in this folder's examples subfolder. Keep the review workbook open for predictions, trace tables, and evidence.

## Guided investigation

1. Open examples/02_for_loop.py. Label the list, one loop variable, repeated body, and first statement after the loop.
2. Predict output for three services, then an empty list. Fill one trace-table row per pass before running. Explain why service is an ordinary name, not a keyword.
3. Open examples/03_while_loop.py. Trace attempt before the condition, the output, and the updated value. Count condition checks as well as body executions.
4. Review AI case B on paper. Find why it cannot reach a stopping value. Propose a bounded repair and test only the repaired copy. Keep Ctrl+C as recovery knowledge, not the lesson method.
5. Use a paper variation with continue before the counter update. Explain why it can break progress. Compare break with continue without executing an unbounded loop.
6. Find the for loops in build_report and main. Draw how each command-result dictionary becomes one output row. Count service queries for the supplied SERVICES list.

Give a reason for each prediction. Run only the supplied working examples or your bounded repair. Compare expected and actual output. Partners switch driver/navigator roles every 15 minutes. The instructor guide schedules demonstrations, paired practice, discussion and this investigation across 180 guided minutes.

## Project and independent work: 180 minutes

Produce for/while trace tables, repair case B in a scratch file, and demonstrate zero, one, and three iterations. Explain which loop fits a known list of services. Annotate the app loop without replacing it with more compact syntax.

Use 60 minutes to trace/review the assigned region, 60 minutes to test a small change or interpretation, and 45 minutes to document evidence. Use the final 15 minutes to save a snapshot and submit. On Day 5, reserve the last hour for demonstrations and submission instead. Small tested edits are expected; writing an application from an empty file is not required.

## Submit and explain

Submit your workbook page, trace or annotated region, exact inputs/commands, and expected/actual evidence. Describe your contribution independently, even if paired. Record an approval decision as accept, edit, or reject with a reason. In sample mode say simulated.

Exit ticket: What does for repeat over? What value changes to stop your while loop?

Support: Use three index cards as list items and a separate counter card for while. Keep indentation visible. Allow a verbal trace.

Optional challenge: Explain why a nested loop over the same service list can multiply work. Count passes for lists of length 3 and 6.

[Back to Start Here](../START-HERE.md)
