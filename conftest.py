# conftest.py
from utils.reporting import summarize_report

def pytest_terminal_summary(terminalreporter, exitstatus):
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    total = passed + failed

    report = summarize_report(passed, failed, total)
    terminalreporter.write_line("=== Jenkins Summary ===")
    terminalreporter.write_line(str(report))
