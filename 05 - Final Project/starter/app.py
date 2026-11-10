"""Menu scaffold supplied to students. Core feature implementations are theirs."""
from pathlib import Path
import sys
import tracker

DATA_PATH = Path(__file__).resolve().with_name("tasks.json")

def show_tasks(tasks):
    if not tasks:
        print("No matching tasks.")
    for task in tasks:
        status = "done" if task["done"] else "open"
        print(f"{task['id']}: {task['title']} [{status}]")

def main():
    try:
        tasks = tracker.load_tasks(DATA_PATH)
    except NotImplementedError:
        print("Starter mode: storage is not implemented yet. Using memory only.")
        tasks = []
    except (ValueError, OSError) as error:
        print(f"Cannot load tasks: {error}. Original file left unchanged.")
        return 1

    while True:
        print("a Add / l List all / o Open only / c Complete / q Quit")
        try:
            choice = input("> ").strip().lower()
            if choice == "q":
                return 0
            if choice == "a":
                title = input("Title: ")
                tracker.add_task(tasks, title)
            elif choice == "c":
                task_id = int(input("Task ID: "))
                tracker.complete_task(tasks, task_id)
            elif choice in ("l", "o"):
                show_tasks(tracker.list_tasks(tasks, only_open=(choice == "o")))
                continue
            else:
                print("Choose a, l, o, c, or q.")
                continue

            try:
                tracker.save_tasks(DATA_PATH, tasks)
            except NotImplementedError:
                print("Changed in memory only. Implement storage on Day 3.")
            except (ValueError, OSError) as error:
                print(f"Save failed: {error}. Latest change is in memory only.")
            else:
                print("Saved.")
        except NotImplementedError as error:
            print(f"Feature pending: {error}")
        except ValueError as error:
            print(f"Invalid input: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting. Only successfully saved changes persist.")
            return 0

if __name__ == "__main__":
    sys.exit(main())
