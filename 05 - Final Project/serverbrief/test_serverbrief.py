"""Run with python -m unittest -v from this folder. No Linux commands run."""
import json
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock
import serverbrief as app

def result(code=0, state="active\n", error=""):
    return {"unit":"sshd.service", "returncode":code,
            "stdout":state, "stderr":"", "error":error}

class ReportTests(unittest.TestCase):
    def test_active(self):
        self.assertEqual(app.classify(result()), "ok")

    def test_inactive(self):
        self.assertEqual(app.classify(result(3, "inactive\n")), "attention")

    def test_failed(self):
        self.assertEqual(app.classify(result(3, "failed\n")), "attention")

    def test_missing_is_unknown(self):
        self.assertEqual(app.classify(result(4, "")), "unknown")

    def test_command_error_is_unknown(self):
        self.assertEqual(app.classify(result(None, "", "timed out")), "unknown")

    def test_contradictory_output_is_unknown(self):
        self.assertEqual(app.classify(result(0, "inactive")), "unknown")

    def test_single_call_and_options(self):
        fake = Mock(return_value=subprocess.CompletedProcess([], 0, "active\n", ""))
        row = app.query_service("sshd.service", runner=fake)
        self.assertEqual(row["returncode"], 0)
        fake.assert_called_once_with(["systemctl", "is-active", "sshd.service"],
                                     capture_output=True, text=True, timeout=5, check=False)

    def test_unapproved_service_never_executes(self):
        fake = Mock()
        with self.assertRaises(ValueError):
            app.query_service("unapproved.service", runner=fake)
        fake.assert_not_called()

    def test_timeout(self):
        fake = Mock(side_effect=subprocess.TimeoutExpired(["systemctl"], 5))
        self.assertEqual(app.classify(app.query_service("sshd.service", fake)), "unknown")

    def test_missing_command(self):
        fake = Mock(side_effect=FileNotFoundError("systemctl missing"))
        self.assertEqual(app.classify(app.query_service("sshd.service", fake)), "unknown")

    def test_sample_report(self):
        rows = app.load_sample(app.SAMPLE)
        report = app.build_report(rows, "simulated")
        self.assertEqual(report["source"], "simulated")
        self.assertEqual([r["status"] for r in report["services"]], ["ok", "attention", "unknown"])

    def test_empty_report(self):
        self.assertEqual(app.build_report([], "simulated")["services"], [])

    def test_bad_sample_schema(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text('[{"unit":"sshd.service"}]', encoding="utf-8")
            with self.assertRaises(ValueError):
                app.load_sample(path)

    def test_bad_returncode_type(self):
        row = result()
        row["returncode"] = True
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "bad.json"
            path.write_text(json.dumps([row]), encoding="utf-8")
            with self.assertRaises(ValueError):
                app.load_sample(path)

if __name__ == "__main__":
    unittest.main()
