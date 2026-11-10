# Annotated resources

Reviewed November 10, 2026. Use one short section or instructor-selected excerpt at the point of need. The course source, examples, fixtures and tests work offline. These links support explanations; they do not replace the daily investigation.

| Resource | When and how | Why / limitation |
| --- | --- | --- |
| [Python introduction](https://docs.python.org/3/tutorial/introduction.html) | Day 1, numbers/strings and assignment, then trace a variation | Primary reference. Ignore newer optional syntax outside our supplied examples |
| [Python control flow](https://docs.python.org/3/tutorial/controlflow.html) | Day 2, for, range, break/continue; Day 3 function definitions | Read just the relevant construct, then fill a trace table |
| [Python modules](https://docs.python.org/3/tutorial/modules.html) | Day 3, import forms and main guard | Explains module execution and name binding; imports do not install packages |
| [Python subprocess](https://docs.python.org/3/library/subprocess.html) | Day 3, run and CompletedProcess, timeout and check | Official options for the command bridge. The supplied code uses APIs available in Python 3.9 |
| [Red Hat Python guidance](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/installing_and_using_dynamic_programming_languages/assembly_introduction-to-python_installing-and-using-dynamic-programming-languages) | Instructor prep and Day 3 interpreter check | RHEL 9 has a vendor-maintained default interpreter and optional versions. Do not replace system Python to match personal-computer advice |
| [RHEL basic system settings](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/htmlsingle/configuring_basic_system_settings/index) | Day 3, service-state and journal inspection sections only | Official RHEL command context. Use local man pages for exact installed behavior. We inspect rather than modify services |
| [CS50 Python loops video and notes](https://cs50.harvard.edu/python/weeks/2/) | Optional Day 2, at most eight instructor-selected minutes on for/while, then a local trace | Official course resource with video/notes. No claimed fixed timestamp, whole-lecture homework or certificate requirement |
| [Python unittest](https://docs.python.org/3/library/unittest.html#basic-example) | Day 4, read one assertion and add one counterexample | Standard-library tests require no installation. Start with provided patterns |
| [GitHub Hello World](https://docs.github.com/en/get-started/using-github/hello-world) | Optional Day 5 publication after clean-copy success | Public accounts are optional; an archive is a full submission route |

Use `man systemctl`, `man journalctl`, `man df`, and `man free` on the assigned VM for exact command options. Prefer a short local demonstration or the notes if a video is blocked or inaccessible. Link to outside videos instead of redistributing them. Provide captions/text where available.

All task data and review drafts are original fictional teaching examples. They do not represent live server observations or a specific AI product's actual transcript. No employment forecast or certification claim is implied.
