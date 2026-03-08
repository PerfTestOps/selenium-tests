# utils/reporting.py
from typing import Dict

def summarize_report(passed: int, failed: int, total: int) -> Dict[str, float]:
    """
    Summarize Jenkins test results.
    """
    return {
        "passed": passed,
        "failed": failed,
        "total": total,
        "pass_percentage": (passed / total * 100) if total > 0 else 0.0
    }
