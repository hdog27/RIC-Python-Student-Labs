"""TaskTrack core. Implement the contracts in Final-Project-and-Rubric.md."""

def validate_tasks(tasks):
    """Day 3: validate the root list and every task, otherwise ValueError."""
    raise NotImplementedError("Day 3: implement validate_tasks")

def add_task(tasks, title):
    """Day 2: append and return a task with a trimmed title and a new ID."""
    raise NotImplementedError("Day 2: implement add_task")

def list_tasks(tasks, only_open=False):
    """Day 2: return a new list of all tasks or only open tasks."""
    raise NotImplementedError("Day 2: implement list_tasks")

def complete_task(tasks, task_id):
    """Day 2: mark a matching stable ID done, or raise ValueError."""
    raise NotImplementedError("Day 2: implement complete_task")

def load_tasks(path):
    """Day 3: missing -> [], invalid -> ValueError, access error -> OSError."""
    raise NotImplementedError("Day 3: implement load_tasks")

def save_tasks(path, tasks):
    """Day 3: validate, write a sibling temporary file, then replace."""
    raise NotImplementedError("Day 3: implement save_tasks")
