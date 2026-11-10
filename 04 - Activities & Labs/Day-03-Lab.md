# Day 3: Imports and RHEL command scripts

Goal: **Explain how a Python process runs a read-only command and interprets its result.**

Vocabulary: modules, import forms, def versus calls, return, subprocess, arguments, stdout, stderr, exit codes, exceptions.

## Read first

Read these sections of the Python reading guide: Functions, arguments, return values, and side effects; Imports; Exceptions and external results. The guide is in `03 - Student Worksheets and Packet`. Today's example is `04_imports_and_functions.py`. Short examples are in this folder's examples subfolder. Keep the review workbook open for predictions, trace tables, and evidence.

## Guided investigation

1. Read examples/04_imports_and_functions.py. Explain import json versus from pathlib import Path. Identify standard-library names, the function definition, its call, and the main guard.
2. Predict what happens when the file runs as a script and when it is imported. Check the prediction in a scratch interpreter session. Imports do not install packages and can execute top-level initialization.
3. Read RHEL-Commands-Inside-Python.md sections 1–2. Translate systemctl is-active sshd.service into a list of executable and arguments. Explain each run option before running anything.
4. Compare the active, inactive, and missing-unit saved records. Trace stdout, stderr, and returncode separately. Distinguish a finished nonzero command from a TimeoutExpired exception.
5. On an assigned RHEL VM, manually inspect whoami, df -h /, and the selected systemctl commands, then run --live. If no VM is available, use the provided sample and label the exercise simulated. Do not claim a live check.
6. Review the bounded journalctl example with your instructor. Explain permissions and why empty visible logs cannot prove there were no events. Record the script-to-command-to-result chain.

Give a reason for each prediction. Run only the supplied working examples or your bounded repair. Compare expected and actual output. Partners switch driver/navigator roles every 15 minutes. The instructor guide schedules demonstrations, paired practice, discussion and this investigation across 180 guided minutes.

## Project and independent work: 180 minutes

Annotate imports and query_service. Create a command translation table and a report explaining source, command exit codes, and unknown results. Add a test for a documented command-error case using a fake runner. No system changes required.

Use 60 minutes to trace/review the assigned region, 60 minutes to test a small change or interpretation, and 45 minutes to document evidence. Use the final 15 minutes to save a snapshot and submit. On Day 5, reserve the last hour for demonstrations and submission instead. Small tested edits are expected; writing an application from an empty file is not required.

## Submit and explain

Submit your workbook page, trace or annotated region, exact inputs/commands, and expected/actual evidence. Describe your contribution independently, even if paired. Record an approval decision as accept, edit, or reject with a reason. In sample mode say simulated.

Exit ticket: Why does import not mean install? Can a nonzero exit code differ from a Python exception?

Support: Separate the Python process, child command, and returned record on paper. Give the command list first, then reveal one keyword option at a time.

Optional challenge: Explain why shell pipes and cd do not act like terminal syntax when passed as ordinary argument-list items.

[Back to Start Here](../START-HERE.md)
