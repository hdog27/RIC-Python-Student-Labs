# Annotated resources

Access reviewed November 10, 2026. Core learning runs offline. These are optional explanations and instructor preparation, not a replacement for labs. Open only the relevant section; do not assign an entire tutorial or full lecture as background homework. Pages may change, so instructors should recheck them before teaching.

| Resource | When and how to use | Why it helps / limits |
| --- | --- | --- |
| [Python downloads](https://www.python.org/downloads/) | Before the course, instructor arranges a school-approved Python installation | Official distribution source. Use an approved supported Python 3 release at least 3.11; do not install during the main lesson |
| [Python 3.11 introduction](https://docs.python.org/3.11/tutorial/introduction.html) | Day 1, read a small numbers/strings example for 5 minutes, then predict and run a variation | Primary explanation of basic expressions. Instructor mediates dense documentation for first-time programmers |
| [Python control flow](https://docs.python.org/3.11/tutorial/controlflow.html) | Day 1 if/else; Day 2 for loops and function definitions. Use one example per concept | Matches the core syntax. Skip match and advanced argument forms |
| [Python data structures](https://docs.python.org/3.11/tutorial/datastructures.html) | Day 2, consult lists and dictionaries while modeling equipment records | Helps students select structures and look up append/key access. Comprehensions are optional |
| [Python input/output](https://docs.python.org/3.11/tutorial/inputoutput.html) | Day 3, focus on files, text encoding and JSON examples | Connects memory to persistent text. Do a local round-trip immediately afterward |
| [JSON module](https://docs.python.org/3.11/library/json.html) | Day 3, look up dumps/loads and JSONDecodeError during malformed-fixture investigation | Defines the actual encoder/decoder behavior. Parsing alone does not validate our task schema |
| [Pathlib](https://docs.python.org/3.11/library/pathlib.html) | Day 3 instructor preparation and optional student reference for read_text/write_text/replace | Cross-platform path tools. Limit student reading to the methods used in the project |
| [Errors and exceptions](https://docs.python.org/3.11/tutorial/errors.html) | Days 3–4, compare a SyntaxError and a ValueError before debugging | Supports specific exception handling and reading tracebacks. Avoid swallowing all errors |
| [Unittest basics](https://docs.python.org/3.11/library/unittest.html#basic-example) | Day 4, read a small TestCase example, then add one original test | Standard-library testing without installation. Focus on assertEqual/assertRaises and discovery |
| [CS50 Python, Week 0: Functions, Variables](https://cs50.harvard.edu/python/weeks/0/) | Optional Day 1 video excerpt, up to 8 minutes on variables/input or string methods, selected during instructor rehearsal | Official Harvard lecture page includes video and notes. Pause for a prediction and a local experiment. Exact excerpt is instructor-selected, not a claimed fixed timestamp. Notes/local demo are the fallback |
| [CS50 Python, Week 5: Unit Tests](https://cs50.harvard.edu/python/weeks/5/) | Optional Day 4 conceptual excerpt, up to 8 minutes on why tests reveal mistakes | Official explanation with video/notes. Some examples use pytest; our unit uses unittest and does not require pytest. Instructor explicitly translates the concept rather than adding another framework |
| [GitHub Hello World](https://docs.github.com/en/get-started/using-github/hello-world) | Optional Day 5 extension after the app works. Walk through a small repository and commit | Official account/repository workflow. Students may submit an archive instead of creating accounts or publishing personal information |

## Source and reuse notes

The curriculum exercises, task data, and project code are original teaching materials. References explain Python and GitHub behavior. We link to third-party videos rather than embedding or redistributing them. Use the provider's captions, transcripts, or notes when available and verify classroom accessibility. No certificate or affiliation with Python, GitHub, Harvard, or CS50 is implied.

## Reading method

Identify one question first. Find the relevant example, predict its result, run it in a scratch file, and explain how it relates to your project. Record sources you actually used in your project's credits.
