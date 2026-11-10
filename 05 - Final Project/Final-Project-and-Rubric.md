# Final project: TaskTrack

Build a command-line application for a student, club member, or volunteer who needs to track tasks. Choose a specific fictional user. The core application works offline using Python's standard library.

## Required behavior

1. Add a task with a trimmed, non-empty title. Allow duplicate titles. Assign a unique positive integer ID greater than the current maximum ID, or 1 for an empty list.
2. List all tasks or only open tasks. Show each task's stable ID, title, and open/done status. Give a useful message when no tasks match.
3. Complete a task by ID. An unknown or invalid ID produces a clear error. Completing an already completed task is harmless and leaves it complete.
4. Save the list as UTF-8 JSON beside app.py. Load it on the next run. A missing file means a new empty tracker.
5. Reject malformed JSON and invalid task data without overwriting the original file. On load failure, exit with a useful error before permitting any save. A missing file and an invalid file are different conditions.
6. Recover from invalid menu choices, blank titles, and non-numeric completion input. Report file access failures clearly. A failed save must not claim success.
7. Keep core logic in functions that tests can call without prompts. The supplied menu code is a scaffold you may adapt.

## Data contract

The root is a list of dictionaries. Each dictionary has **exactly** these fields:

```json
{"id": 7, "title": "Practice presentation", "done": false}
```

`id` is a positive integer, excluding booleans. IDs are unique within the list. `title` is a string with at least one non-whitespace character. `done` is a true boolean, never a string such as "yes". Reject extra/missing fields. The loader validates existing records without rewriting titles. New task titles are trimmed by add_task. Use `type(value) is int` when validating IDs because Python booleans are also instances of int.

## Required functions in tracker.py

| Function | Contract |
| --- | --- |
| `validate_tasks(tasks)` | Return None for valid data, otherwise raise ValueError |
| `add_task(tasks, title)` | Validate input. Append a new dictionary to tasks and return the new dictionary. Invalid title: ValueError, list unchanged |
| `list_tasks(tasks, only_open=False)` | Return a new list containing matching task dictionaries in input order. Do not change tasks. A shallow list copy is sufficient |
| `complete_task(tasks, task_id)` | Mark matching task done and return that dictionary. Invalid/unknown ID: ValueError, list unchanged |
| `load_tasks(path)` | Return validated tasks. Missing file: []. Invalid JSON/schema/UTF-8: ValueError. Other file access problems: OSError |
| `save_tasks(path, tasks)` | Validate, save using UTF-8 JSON, return None. Invalid data: ValueError. File access problem: OSError. Preserve an existing target if writing the temporary file fails |

`path` accepts pathlib.Path or a path string. Parent folder must already exist. Write a sibling temporary file, then replace the target after successful writing. Assume one running app per data file; concurrency, encryption, and account management are outside this unit. Core functions may assume valid task collections after the loader validates them, except validate_tasks and save_tasks must validate all stored records.

## Milestones

| Day | Acceptance checkpoint |
| --- | --- |
| 1 | A user story, menu sketch, and title-entry prototype |
| 2 | Add/list/complete in memory, including stable IDs |
| 3 | Save/load, restart evidence, and invalid-file preservation |
| 4 | Full menu, supplied tests, four original tests, debugging log |
| 5 | Clean-copy review, final fixes, README and demonstration |

## Manual acceptance checklist

Use a fresh writable copy with fictional data. Record inputs and actual outputs.

- [ ] Launch without tasks.json. List tasks. See a clear empty message.
- [ ] Add `Read a chapter` and `Practice presentation`. Verify different IDs and open status.
- [ ] Mark the second ID complete. All view shows it done. Open-only view excludes it.
- [ ] Quit and restart. Titles, IDs, and completion state survive.
- [ ] Enter an invalid menu choice, a blank title, letters for an ID, and an unknown ID. Get useful feedback without a crash or false success.
- [ ] Complete an already completed task again. It stays complete.
- [ ] Replace only a scratch copy's save file with malformed JSON. Launch. Confirm a useful error, a nonzero exit, and identical original bytes afterward.
- [ ] Try a valid JSON document with wrong fields or duplicate IDs. Confirm rejection and preservation.
- [ ] Run all automated tests. Add four original tests covering an edge case, invalid input, persistence, and a bug or extension.
- [ ] Ask someone to launch a clean copy from your README without spoken help.

## Rubric: 100 points

Each row has four anchors. Award the listed value that best matches the evidence. Partial credit is deliberate and specific. Cosmetic polish does not replace correctness.

| Criterion | Complete | Mostly complete | Partial | Not evidenced |
| --- | --- | --- | --- | --- |
| Core add/list/complete, 25 | 25: all required flows, stable IDs and open filter work | 19: one flow has a reproducible defect | 10: only one or two flows work | 0: no running core |
| Persistence and data protection, 20 | 20: restart works and both invalid JSON and schema preserve original bytes | 15: restart works, one error condition fails | 8: saves or loads but round-trip unreliable | 0: no persistence |
| Validation and errors, 15 | 15: blank/menu/ID/file errors handled clearly | 11: one category fails | 6: several errors crash or mislead | 0: no handling shown |
| Tests and debugging evidence, 15 | 15: supplied suite plus four meaningful original tests and a reproduced bug/repair | 11: suite passes, fewer original tests or weak log | 6: some repeatable testing | 0: no test evidence |
| Code clarity and explanation, 10 | 10: functions, readable names and independent explanation | 7: understandable with minor coupling | 4: difficult to follow or explain | 0: cannot explain submitted work |
| README and reproducibility, 10 | 10: clean-copy reviewer runs app and tests from instructions | 7: one missing detail | 4: several undocumented steps | 0: no usable instructions |
| Demo, reflection and attribution, 5 | 5: demonstrates core, explains limitation and credits help | 4: one element missing | 2: minimal demonstration | 0: absent |

Optional extensions support learning but earn no automatic bonus. Examples: title search, CSV export, task categories, or priority. Finish and test the required core first. Extensions may add fields only if you update validation, tests, and documentation and preserve an importable core compatible with the supplied contracts for grading.

## Submission

Submit source, tests, README, manual-check evidence, debugging log, and a three-minute demo or equivalent recorded explanation. Include your workbook and reflection. Use a repository link **or an archive**. A public GitHub profile is optional. For a team of two, name each contribution and have each person explain a function and test.

AI policy: make your own prediction and first attempt before asking for assistance. You may use AI for explanations or small debugging hints when the instructor permits it. Record the tool, prompt purpose, and what you accepted or rejected in your README. Verify every adopted change with tests. You must be able to explain submitted code. Assessments are individual without AI.

## Portfolio language

Suggested description, edit to match your actual work: "Built a Python command-line task tracker with JSON persistence, input validation, and automated tests. Documented setup and demonstrated recovery from malformed save data."

State specific features and your contribution. Do not claim professional experience, certification, production deployment, or security guarantees from this classroom project. Include a fictional-data screenshot or short demo and working setup instructions.
