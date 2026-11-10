"""Acceptance checks. Errors are expected while starter functions are incomplete."""
import tempfile
import unittest
from pathlib import Path
from tracker import (add_task, list_tasks, complete_task, validate_tasks,
                     load_tasks, save_tasks)

class TrackerTests(unittest.TestCase):
    def test_add_trims_and_allocates_id(self):
        tasks = [{"id": 7, "title": "Existing", "done": False}]
        created = add_task(tasks, "  New  ")
        self.assertEqual(created, {"id": 8, "title": "New", "done": False})
        self.assertEqual(tasks[-1], created)

    def test_blank_rejected_without_mutation(self):
        tasks = []
        with self.assertRaises(ValueError):
            add_task(tasks, "   ")
        self.assertEqual(tasks, [])

    def test_open_filter_preserves_original(self):
        tasks = [{"id": 1, "title": "A", "done": False},
                 {"id": 7, "title": "B", "done": True}]
        self.assertEqual([t["id"] for t in list_tasks(tasks, True)], [1])
        self.assertEqual(len(tasks), 2)
        self.assertIsNot(list_tasks(tasks), tasks)

    def test_complete_uses_stable_id(self):
        tasks = [{"id": 7, "title": "A", "done": False}]
        self.assertTrue(complete_task(tasks, 7)["done"])
        self.assertTrue(tasks[0]["done"])
        with self.assertRaises(ValueError):
            complete_task(tasks, 99)

    def test_schema_rejects_non_boolean(self):
        with self.assertRaises(ValueError):
            validate_tasks([{"id": 1, "title": "A", "done": "yes"}])

    def test_missing_file_starts_empty(self):
        with tempfile.TemporaryDirectory() as folder:
            self.assertEqual(load_tasks(Path(folder) / "missing.json"), [])

    def test_save_load_round_trip(self):
        tasks = [{"id": 7, "title": "Café practice", "done": True}]
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            save_tasks(path, tasks)
            self.assertEqual(load_tasks(path), tasks)

    def test_bad_json_preserved(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "tasks.json"
            path.write_bytes(b'{broken')
            with self.assertRaises(ValueError):
                load_tasks(path)
            self.assertEqual(path.read_bytes(), b'{broken')

if __name__ == "__main__":
    unittest.main()
