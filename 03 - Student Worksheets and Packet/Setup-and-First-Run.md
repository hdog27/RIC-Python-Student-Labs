# Setup and first run

Allow 30 minutes. Work in a folder you can write to, such as Documents. Avoid running directly inside a ZIP archive.

1. Download and extract the student repository. Open the extracted folder in your editor. Use a school-approved editor, Python's IDLE, or VS Code.
2. Open a terminal in that folder. On Windows, try `py --version`, then `python --version`. On macOS/Linux, try `python3 --version`. You need Python 3.11 or later. If no command works, ask the instructor to arrange installation from https://www.python.org/downloads/ or a managed school installation. Do not change school security settings.
3. The examples below use `python`. Replace it consistently with the command that worked for you, such as `py` or `python3`.
4. Run the setup check from the repository root:

```text
python "04 - Activities & Labs/check_setup.py"
```

Expected: Python version, a writable temporary folder check, JSON round-trip success, and `Setup OK`. No package installation is required.

5. Run the Day 1 example:

```text
python "04 - Activities & Labs/demos/day1_example.py"
```

Enter `12`. You should see `Three sessions take 36 minutes.`

6. Copy the **entire** folder `05 - Final Project/starter` into your own workspace and call the copy `tasktrack`. It should contain `app.py`, `tracker.py`, `test_tracker.py`, and a README template. Open a terminal **inside your tasktrack copy**. Use the editor's Open Folder command to make this easy.
7. Run `python app.py`. The starter opens its menu. Choosing `q` exits. Choosing a feature before you implement it prints a reminder rather than pretending to work.
8. Run `python -m unittest -v`. Initially, incomplete core functions cause expected errors. Save this baseline. By Friday these checks should pass and you should have added at least four original tests.

## If something goes wrong

| Symptom | Next action |
| --- | --- |
| Python opens a store page | Ask the instructor to check the installed Python interpreter and app execution alias |
| `can't open file` | Confirm the terminal folder and quote paths containing spaces |
| `>>>` prompt | You are in the Python shell. Enter `exit()` and run the command in the terminal |
| A file ends in `.py.txt` | Enable file extensions and save as a Python file |
| `PermissionError` | Move your working copy to a writable student folder |
| `ModuleNotFoundError: tracker` | Keep `app.py`, `tracker.py`, and the tests in the same folder |
| My edits do nothing | Save the file and check that the terminal is running the same copy |

## No internet or GitHub account?

An instructor can provide an extracted offline copy and an installed interpreter. All core examples, sample data, and tests run offline. Save daily snapshots as `day1.zip`, `day2.zip`, etc. Submit an archive instead of a GitHub link. GitHub is an optional publication route, not a course prerequisite.
