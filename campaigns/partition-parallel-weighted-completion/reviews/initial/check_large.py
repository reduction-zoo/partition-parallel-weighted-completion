"""Independent high-bit end-to-end checks for the submitted maps."""

import json
import subprocess
import sys
from pathlib import Path


CANDIDATE = Path(__file__).resolve().parents[2] / "work" / "algorithm.py"
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)


def call(payload, extract=False):
    args = [sys.executable, str(CANDIDATE)] + (["--extract"] if extract else [])
    result = subprocess.run(args, input=json.dumps(payload), text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(result.stderr)
    return json.loads(result.stdout)


def check_pair(left, right):
    source = {"numbers": [left, right]}
    target = call(source)
    assert target["machines"] == 2
    assert target["processing_times"] == [2 * left, 2 * right]
    assert target["weights"] == [2 * left, 2 * right]
    # Independent two-job optimum: one job per machine, both starting at zero.
    best_cost = 4 * (left * left + right * right)
    if left == right:
        assert best_cost == target["K"]
        for assignment, expected in [([0, 1], [0]), ([1, 0], [1])]:
            schedule = {"machines": assignment, "starts": [0, 0]}
            assert call({"source": source, "target_solution": schedule}, True) == {"indices": expected}
    else:
        assert best_cost > target["K"]
        assert call({"source": source, "target_solution": {"no_solution": True}}, True) == {"no_solution": True}


if __name__ == "__main__":
    large = (1 << 2048) + 12345
    check_pair(large, large)
    check_pair(large, large + 1)
    # The input JSON remains under Python's decimal-digit limit; K does not.
    check_pair(1 << 8192, 1 << 8192)
    print("large-bit forward and recovery checks passed")
