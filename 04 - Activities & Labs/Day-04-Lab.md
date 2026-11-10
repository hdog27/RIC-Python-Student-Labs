# Day 4: Review AI drafts and unnecessary work

Goal: **Support an accept, edit, or reject decision with a trace and repeatable evidence.**

Vocabulary: counterexamples, equality versus membership, bounded loops, command handling, repeated calls, tests, approval decisions.

## Read first

Read these sections of the Python reading guide: AI-assisted reading and review. The guide is in `03 - Student Worksheets and Packet`. Today's example is `AI-Review-Cases.md`. Short examples are in this folder's examples subfolder. Keep the review workbook open for predictions, trace tables, and evidence.

## Guided investigation

1. Review case A before executing any repair. Predict the result for inactive. Explain why a plausible English explanation of the code can still be wrong.
2. Specify expected outcomes for active, inactive, failed, missing output, and command errors. Trace which evidence the draft ignores. Repair only a scratch copy and run counterexamples.
3. Review case C. Count child-process calls for two services. Identify the missing timeout, shell interpretation, discarded exit code, and duplicated calls.
4. Replace real querying with a fake function that records calls. Compare a repeated-read draft with a once-per-unit version. Keep reported results equivalent for fixed fake inputs and report exact call counts.
5. Optionally ask an AI assistant to explain a small snippet or suggest tests. Record a suggestion and a reason to accept, edit, or reject it. Without an account, review the supplied written draft with a peer.
6. Run the supplied tests and your new cases. Explain what each test does and what it cannot prove. A short function or passing suite alone is not an approval argument.

Give a reason for each prediction. Run only the supplied working examples or your bounded repair. Compare expected and actual output. Partners switch driver/navigator roles every 15 minutes. The instructor guide schedules demonstrations, paired practice, discussion and this investigation across 180 guided minutes.

## Project and independent work: 180 minutes

Complete a review memo for cases A–C, a small repaired example, and a measured command-call reduction. Add at least three original tests total: a boundary or counterexample, an error path, and an efficiency/behavior check. Record attributions and unresolved assumptions.

Use 60 minutes to trace/review the assigned region, 60 minutes to test a small change or interpretation, and 45 minutes to document evidence. Use the final 15 minutes to save a snapshot and submit. On Day 5, reserve the last hour for demonstrations and submission instead. Small tested edits are expected; writing an application from an empty file is not required.

## Submit and explain

Submit your workbook page, trace or annotated region, exact inputs/commands, and expected/actual evidence. Describe your contribution independently, even if paired. Record an approval decision as accept, edit, or reject with a reason. In sample mode say simulated.

Exit ticket: What counterexample changed your review decision? Which unnecessary work did you remove, and how did you measure it?

Support: Give a fixed fake return value and a list that records calls. Count operations before introducing timing or mocking syntax. Use ordinary loops when clearer.

Optional challenge: Compare a list scan with a set-membership check, preserving order requirements. Explain when the optimization adds complexity without useful benefit.

[Back to Start Here](../START-HERE.md)
