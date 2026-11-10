"""Day 4 investigation: repair the implementation, preserve the tests."""
import unittest

def count_open(tasks):
    count = 1
    for task in tasks:
        if task["done"]:
            count += 1
    return count

class SummaryTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(count_open([]), 0)

    def test_mixed(self):
        tasks = [{"done": False}, {"done": True}, {"done": False}]
        self.assertEqual(count_open(tasks), 2)

if __name__ == "__main__":
    unittest.main()
