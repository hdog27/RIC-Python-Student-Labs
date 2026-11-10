# Start here

## 1. Run the supplied example

Download **Code > Download ZIP** from the repository, extract it, then open the extracted folder in your editor. On Windows, check `python --version` or `py --version`. On macOS/Linux, check `python3 --version`. Use a school-approved Python 3 installation. The source uses Python 3.9-compatible syntax so it can also run with RHEL 9's vendor-maintained interpreter. On personal computers, use a current supported Python 3 release. No pip packages are required.

Commands below use `python`; replace it consistently with the command that works on your computer. From the extracted repository folder:

```text
python "05 - Final Project/serverbrief/serverbrief.py"
```

Expected: JSON labeled `"source": "simulated"`, with one ok, one attention, and one unknown service. These are fictional saved results. Your own server has not been checked.

Then open a terminal **inside** `05 - Final Project/serverbrief` and run:

```text
python -m unittest -v
```

The supplied 14 tests should pass before you change anything. Copy the serverbrief folder to your own writable workspace and work on that copy. Save a daily snapshot. Never run from inside a ZIP archive.

If the command cannot find a file, check the terminal's current folder and quote paths containing spaces. If you see `>>>`, enter `exit()` to leave the Python shell. If Python is absent, use the instructor's approved installation. Do not change school security settings.

## 2. Open only today's lesson

Each daily page tells you what to read, what to run, what to review, and what to submit. Use the matching slide deck when your instructor presents it. Keep your responses in [the review workbook](03%20-%20Student%20Worksheets%20and%20Packet/Review-Workbook.md).

| Day | Lesson | Slides |
| --- | --- | --- |
| 1 | [Read variables and decisions](04%20-%20Activities%20%26%20Labs/Day-01-Lab.md) | [Day 1](02%20-%20Presentations/Day-01-Why-Python-and-Reading-Code.pptx) |
| 2 | [Trace for and while loops](04%20-%20Activities%20%26%20Labs/Day-02-Lab.md) | [Day 2](02%20-%20Presentations/Day-02-For-and-While-Loops.pptx) |
| 3 | [Read imports and RHEL command scripts](04%20-%20Activities%20%26%20Labs/Day-03-Lab.md) | [Day 3](02%20-%20Presentations/Day-03-Imports-and-RHEL-Commands.pptx) |
| 4 | [Review AI drafts and efficiency](04%20-%20Activities%20%26%20Labs/Day-04-Lab.md) | [Day 4](02%20-%20Presentations/Day-04-AI-Review-and-Efficiency.pptx) |
| 5 | [Explain and deliver reviewed work](04%20-%20Activities%20%26%20Labs/Day-05-Lab.md) | [Day 5](02%20-%20Presentations/Day-05-Review-and-Demonstration.pptx) |

## 3. Keep these references nearby

- [Python reading guide](03%20-%20Student%20Worksheets%20and%20Packet/Python-Reading-Guide.md): plain-language explanations of syntax and execution.
- [RHEL commands inside Python](04%20-%20Activities%20%26%20Labs/RHEL-Commands-Inside-Python.md): the command-to-script bridge, with every option explained.
- [Final project and rubric](05%20-%20Final%20Project/Final-Project-and-Rubric.md): what to submit and how it is assessed.

A public GitHub profile and an AI account are optional. You can submit an archive and use the provided draft-review cases offline. Ask your instructor before live mode. It queries the assigned Linux VM, never a remote server automatically.
