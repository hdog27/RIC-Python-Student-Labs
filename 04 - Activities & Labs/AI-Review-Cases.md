# Three draft reviews

These are deliberately constructed teaching drafts, representative of mistakes a coding assistant or a human could make. They are not transcripts of a particular AI product. Review them on paper first. Do not execute the flawed snippets. Use scratch files with fake inputs for repairs. No AI account is necessary.

For each case: explain the intent, trace the actual behavior, name a risk/defect, propose the smallest justified change, give a counterexample, and state what evidence supports approval. The private instructor key contains sample repairs.

## A. Service state

```python
state = "inactive"
if "active" in state:
    print("healthy")
else:
    print("needs review")
```

Review `in` versus `==`. Try active, inactive, failed, and an empty string in a scratch test. Also ask what the command exit code says. A string alone is incomplete evidence about command success.

## B. Bounded retries

```python
attempt = 0
while attempt < 3:
    print("Checking again")
```

Trace attempt through four imagined iterations without running it. Which value or condition could stop it? Define a maximum number of attempts before repairing it. A real retry loop would also need a delay and a reason to retry. We do not poll real services in this exercise.

## C. External commands and repeated work

```python
def read_state(unit):
    return subprocess.run("systemctl is-active " + unit,
                          shell=True, capture_output=True,
                          text=True).stdout.strip()

for unit in services:
    print(unit, read_state(unit), read_state(unit))
```

Assume services contains two entries. Count external commands. Review the string command, shell interpretation, timeout, missing executable, nonzero exit code, and repeated reads that could disagree. Explain why changing just shell=True to shell=False while retaining a command string is an incomplete repair. Use the supplied app's query_service as a reading reference after your own first review. Test repairs with a fake runner instead of real commands.

## Optional AI-assisted review

Prompt: "Explain this Python snippet line by line for a beginner. Identify variable types, the repeated block, and the stop condition. List assumptions and propose small counterexamples. Do not execute commands."

Then challenge the explanation with your own trace and tests. Log the suggestion, your decision, and your evidence. Accept, edit, or reject suggestions for a stated reason. A confident explanation is not proof. Do not upload real server logs or private credentials. Use the supplied fictional data.
