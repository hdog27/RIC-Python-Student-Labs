# Post-assessment

15 minutes, individual, no notes or AI. Two points per item, 20 total. Explain reasoning. The pre-assessment guides support; it is not an entry requirement.

1. Given `used = 79; limit = 80`, explain the role of each name and the value/type of `used >= limit`.

2. How do assignment and comparison differ? Why might `int(input(...))` raise an error?

3. Trace `for name in ["x", "y", "z"]: print(name)`. What changes with an empty list?

4. Trace a while loop starting n at 1, checking n < 4, printing n, then adding 1. What stops it?

5. A continue occurs before a while counter update. Explain the risk and a repair that guarantees progress.

6. What does `import subprocess` make available? Why can importing an unfamiliar module do work beyond defining functions?

7. Why can tests import a file without calling its guarded main? How does a returned result differ from displayed output?

8. Explain the command list, capture_output=True, text=True, and timeout=5 in subprocess.run.

9. A service query times out or says a unit is missing. Why must a report preserve unknown rather than claim healthy?

10. Give evidence for approving a repair to substring-based state detection and a change from two queries per service to one.

Confidence (1–5): reading code ___ tracing loops ___ reviewing commands ___
