# Day 3: Saving data safely

**Learning target:** Save and load task data, distinguish a missing file from malformed content, and preserve a bad file for recovery.

**You need:** your editor, Python, a writable project folder, and today's workbook page. The guided lab takes 50 minutes plus a 15-minute share-out. Project work takes a separate 180 minutes. Pairing is encouraged; change driver every 15 minutes.

## Predict before running

Your save file contains half a JSON object. Should loading it silently return an empty list? What could the next save destroy?

Write your prediction and the reason. Run a small experiment to check it.

## Guided lab: Investigate JSON files

1. Create `day3_storage.py`. Import json and Path. Work with a scratch file in your own folder.
2. Encode a short list of equipment dictionaries with `json.dumps(data, indent=2)` and write UTF-8 text. Read and decode it. Compare the loaded value with the original.
3. Inspect the provided sample and malformed JSON fixtures. Before running anything, predict which will parse.
4. Try a missing file. Catch FileNotFoundError specifically and choose an empty initial list for a new app.
5. Try malformed JSON. Catch JSONDecodeError and report the problem. Keep the original bytes unchanged. Never treat this as a successful empty load.
6. Try syntactically valid JSON with the wrong fields. Explain why successful parsing does not establish that it is valid task data.

## Project work

Implement `validate_tasks`, `load_tasks`, and `save_tasks` in tracker.py. Integrate them with the supplied app menu. Pass the public storage tests. Restart the app and verify saved tasks survive. Copy a corrupt fixture to a scratch tasks.json, run the app, and verify the bad file remains unchanged.

Work in three 60-minute blocks: build the core milestone, test it with a peer, then improve and document it. Before adding an extension, demonstrate the required milestone to your instructor.

## Checkpoint and submission

Submit JSON round-trip, preserved malformed file, missing-file behavior, passing storage tests, and before/after restart evidence. Include exact commands and inputs so someone else can repeat your result. A screenshot helps but does not replace your source files.

## Exit ticket

What is the difference between JSON parsing and schema validation? Why should a failed load stop the app from saving?

## Need a hint?

State the smallest input that fails. Locate the matching concept in the Python reference sheet. Write the expected result before asking for a code suggestion. Ask your instructor for a targeted hint if you remain stuck after ten minutes.

## Extension

Explain how the supplied temporary-file-and-replace save pattern reduces the chance of a partial target file. Multi-process editing remains out of scope.
