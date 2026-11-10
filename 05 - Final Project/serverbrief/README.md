# ServerBrief working copy

Python standard library only. The source uses Python 3.9-compatible syntax for the assigned RHEL 9 interpreter. Use a current supported Python 3 on personal computers. Open a terminal in this folder:

```text
python serverbrief.py
python -m unittest -v
python serverbrief.py --output review-report.json
```

Use python, py, or python3 as selected during setup. Default mode reads fictional sample-results.json beside the script and labels output simulated. No Linux commands run in that mode or in the tests. Fourteen supplied tests pass before modifications. Use a new output filename because existing files are protected.

On an instructor-assigned RHEL VM only: `python3 serverbrief.py --live`. Live mode queries local sshd.service and crond.service with systemctl is-active, ordinary-account permissions, and a five-second timeout per query. It does not connect to a remote server or restart services. Missing commands, unavailable systemd, and uncertain results remain unknown.

For your submission, add your user need, annotated walkthrough, review memo, repaired exercise modules, original tests, call-count comparison, and a demo. Document exact commands, known limitations, contributions and all AI/peer/source credits. The baseline application is supplied course code, not your original implementation. Consult the project rubric one folder above.
