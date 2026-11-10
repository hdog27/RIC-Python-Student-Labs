# Day 2: Data and functions

**Learning target:** Represent several tasks, implement add/list/complete functions, and explain why IDs are different from list positions.

**You need:** your editor, Python, a writable project folder, and today's workbook page. The guided lab takes 50 minutes plus a 15-minute share-out. Project work takes a separate 180 minutes. Pairing is encouraged; change driver every 15 minutes.

## Predict before running

A task has ID 7 and sits at index 0. Which value should a user type to complete it? What happens if you use tasks[7]?

Write your prediction and the reason. Run a small experiment to check it.

## Guided lab: Organize an equipment checkout list

1. Create `day2_equipment.py`. Represent three fictional equipment items as dictionaries with id, name, and checked_out fields. Store them in a list.
2. Write `available_names(items)` that returns a new list of the names whose checked_out value is False. Keep printing outside the function.
3. Trace the loop by hand with an empty list and with all items checked out.
4. Write a function that finds an item by ID and changes its checked_out value. Raise ValueError for an unknown ID.
5. Try IDs 1, 7, and 99 on a list with IDs 1 and 7. Check that an ID is not being used as an index.
6. Swap driver/navigator roles after 15 minutes. Have your partner explain one return value and one side effect.

## Project work

Open your tracker.py copy. Implement `add_task`, `list_tasks`, and `complete_task` to the contracts in the project specification. Use an empty list in the Python shell to exercise them. Use a temporary in-memory script if the full menu still needs Day 3 storage. Attempt the matching public tests by name.

Work in three 60-minute blocks: build the core milestone, test it with a peer, then improve and document it. Before adding an extension, demonstrate the required milestone to your instructor.

## Checkpoint and submission

Submit equipment exercise, a function trace, three tracker functions, and add/list/complete evidence using IDs 1 and 7. Include exact commands and inputs so someone else can repeat your result. A screenshot helps but does not replace your source files.

## Exit ticket

How does a function returning a string differ from printing one? Why should task IDs stay stable?

## Need a hint?

State the smallest input that fails. Locate the matching concept in the Python reference sheet. Write the expected result before asking for a code suggestion. Ask your instructor for a targeted hint if you remain stuck after ten minutes.

## Extension

Implement case-insensitive title search as a separate function without changing the required interfaces.
