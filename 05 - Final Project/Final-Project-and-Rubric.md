# Final project: review and explain ServerBrief

You are reviewing a small automation helper for a fictional Linux administrator. Begin with the supplied, runnable serverbrief folder. Your job is to understand its behavior, evaluate draft suggestions, test small changes, and prepare a report another person can trust within its stated limits.

## Deliverables

1. A copy of the supplied app, sample JSON, tests, and a README. Source credit must identify the course scaffold. An unchanged baseline app is acceptable if your required repairs and efficiency comparison are in separate scratch modules with tests.
2. An annotated walkthrough: explain variables/types, an if branch, a for loop, a bounded while loop, function calls/returns, imports, the main guard, and subprocess options. A separate bounded while example is expected; do not add an unnecessary while loop to the app.
3. A review memo for all three AI review cases. State purpose, actual behavior, a counterexample/risk, accept/edit/reject decision, and a justified repair or rejection. Include a repaired copy of the state-comparison and bounded-loop exercises.
4. An efficiency comparison using a fake service query. Show calls before and after removing a repeated query. For two unique services, the draft makes four calls and the revised approach should make two while preserving intended output for fixed fake results. Explain why fewer external calls matter. No unsupported claim about universal runtime speed is required.
5. All 14 supplied tests plus at least three original tests: a counterexample/boundary, an error path, and a behavior/operation-count check for your change. Test repairs independently. Real servers are not needed for tests.
6. A saved JSON report clearly labeled simulated or live, a clean-copy peer review, the workbook/reflection, and a three-minute demonstration. A live RHEL observation is optional if the instructor cannot provide a suitable VM.

## Reporting contract

Default mode loads the fictional sample beside serverbrief.py. Live mode runs locally on the assigned Linux VM and queries only configured allowlisted services. It performs no administrative changes. Classification: exact active plus returncode 0 and no command exception gives ok. Exact inactive/failed plus nonzero returncode and no command exception gives attention. Missing/contradictory evidence, timeout, missing executable, and unrecognized state give unknown. These are classroom policies, not a comprehensive health assessment.

Retain source, each unit's state, returncode, stderr, and error. Do not relabel simulated observations as live. The script's own exit 0 means it created a report, not that every service is healthy. A new --output path creates JSON; an existing file must remain unchanged. Explain this local file-writing side effect.

## Acceptance checklist

- [ ] A new reader can run sample mode and all tests from the README.
- [ ] Sample output contains source simulated and ok/attention/unknown records.
- [ ] Your walkthrough correctly predicts new inputs and loop termination.
- [ ] You explain each import and identify any external process or file write.
- [ ] State-comparison repair rejects the inactive substring trap.
- [ ] Bounded-loop repair stops and handles zero iterations deliberately.
- [ ] Efficiency evidence counts calls and checks equivalent intended results.
- [ ] Three original tests exercise distinct cases and pass.
- [ ] Missing commands/timeouts remain unknown; no automatic restarts or sudo escalation.
- [ ] Existing report files survive an attempted overwrite.
- [ ] Review memo credits sources/assistance and states limitations.

## Rubric: 100 points

| Criterion | Full evidence | Partial evidence | Minimal/absent |
| --- | --- | --- | --- |
| Code reading and explanation, 35 | 35: accurate walkthrough of all listed constructs and independent trace of a new case | 25: mostly accurate, one major gap; 15: several gaps | 5: reads syntax without explaining behavior; 0: absent |
| Review decisions and repairs, 25 | 25: all three cases, concrete counterexamples, justified repairs/rejection | 18: two sound cases; 10: one sound case | 4: unsupported approval; 0: absent |
| Tests and evidence, 15 | 15: baseline plus three distinct original passing tests and exact reproduction | 11: incomplete original coverage; 6: manual evidence only | 0: no repeatable evidence |
| Efficiency reasoning, 10 | 10: counts 4 versus 2 queries, checks behavior, explains tradeoff | 7: correct count with weak equivalence check; 4: plausible idea only | 0: unsupported or absent |
| Report, README, demo and attribution, 15 | 15: clean-copy success, honest source label/limits, independent explanation and credits | 11: one missing element; 6: several gaps | 0: unusable or absent |

Choose the listed level that best fits observed evidence. Scoring emphasizes understanding and judgment. Typing speed, lines of code, public GitHub participation, or memorized library details do not earn points. Equivalent repairs and plain loops are welcome.

## AI assistance and portfolio language

AI assistance is optional. Make a prediction and first review before seeking help. Record what you accepted, edited, or rejected and how you tested it. You are accountable for approved behavior. Assessments remain individual without AI. Do not share real logs, credentials, or private system data.

Example portfolio statement, edit to match your work: "Reviewed a Python Linux service-reporting script, traced loops and subprocess results, repaired faulty draft logic, and tested a reduction in repeated command calls. Documented report limitations and reproducible sample execution."

Submit a repository link or archive. Team members name their individual contributions and each explain a function, loop and test. Use fictional data for public demonstration media.
