"""Independent source and scheduling oracles for the prepared corpus."""

import argparse
import itertools
import json
import subprocess
import sys
from pathlib import Path

from z3 import And, Int, Or, Solver, Sum, sat, unsat

ROOT = Path(__file__).resolve().parents[3]
WORK = Path(__file__).resolve().parent


def source_solutions(numbers):
    total = sum(numbers)
    return [list(bits) for length in range(len(numbers) + 1)
            for bits in itertools.combinations(range(len(numbers)), length)
            if 2 * sum(numbers[i] for i in bits) == total]


def valid_source(numbers, output):
    if output == {"no_solution": True}:
        return not source_solutions(numbers)
    if not isinstance(output, dict) or set(output) != {"indices"}:
        return False
    indices = output["indices"]
    return (isinstance(indices, list) and all(type(i) is int and 0 <= i < len(numbers) for i in indices)
            and len(set(indices)) == len(indices)
            and 2 * sum(numbers[i] for i in indices) == sum(numbers))


def valid_target(target, output):
    if output == {"no_solution": True}:
        return solve_target(target, limit=1) == []
    if not isinstance(output, dict) or set(output) != {"machines", "starts"}:
        return False
    machines, starts = output["machines"], output["starts"]
    p, w, m, K = (target[k] for k in ("processing_times", "weights", "machines", "K"))
    n = len(p)
    if not (len(w) == len(machines) == len(starts) == n and
            all(type(x) is int and 0 <= x < m for x in machines) and
            all(type(x) is int and x >= 0 for x in starts)):
        return False
    if any(machines[i] == machines[j] and
           starts[i] < starts[j] + p[j] and starts[j] < starts[i] + p[i]
           for i in range(n) for j in range(i + 1, n)):
        return False
    return sum(w[i] * (starts[i] + p[i]) for i in range(n)) <= K


def solve_target(target, limit=2):
    p, w, m, K = (target[k] for k in ("processing_times", "weights", "machines", "K"))
    n = len(p)
    assert n >= 1 and len(w) == n and m >= 1 and K >= 0
    assert all(type(x) is int and x > 0 for x in p + w)
    solver = Solver()
    machines = [Int(f"machine_{i}") for i in range(n)]
    starts = [Int(f"start_{i}") for i in range(n)]
    for i in range(n):
        solver.add(And(machines[i] >= 0, machines[i] < m, starts[i] >= 0))
    for i in range(n):
        for j in range(i + 1, n):
            solver.add(Or(machines[i] != machines[j],
                          starts[i] + p[i] <= starts[j],
                          starts[j] + p[j] <= starts[i]))
    solver.add(Sum([w[i] * (starts[i] + p[i]) for i in range(n)]) <= K)
    outputs = []
    for _ in range(limit):
        status = solver.check()
        if status == unsat:
            break
        if status != sat:
            raise RuntimeError(f"target oracle inconclusive: {status}")
        model = solver.model()
        assignment = [model.eval(v).as_long() for v in machines]
        start_values = [model.eval(v).as_long() for v in starts]
        output = {"machines": assignment, "starts": start_values}
        assert valid_target(target, output)
        outputs.append(output)
        solver.add(Or(*[v != value for v, value in zip(machines + starts, assignment + start_values)]))
    return outputs


def run_candidate(path, payload, extract=False):
    command = [sys.executable, str(path)] + (["--extract"] if extract else [])
    result = subprocess.run(command, input=json.dumps(payload), text=True, capture_output=True, check=True)
    return json.loads(result.stdout)


def self_test(cases):
    subprocess.run([sys.executable, str(ROOT / "research/validate_preparation.py"), str(WORK / "cases.json")], check=True)
    assert source_solutions([1]) == []
    assert source_solutions([1, 1]) == [[0], [1]]
    assert source_solutions([1, 2, 3]) == [[2], [0, 1]]
    assert not valid_source([1, 2, 3], {"indices": [0]})
    assert not valid_source([1, 1], {"indices": [0, 0]})
    assert not valid_source([1, 1], {"no_solution": True})
    assert not valid_source([1], {"indices": []})
    target = {"processing_times": [1, 1], "weights": [1, 1], "machines": 1, "K": 3}
    assert valid_target(target, {"machines": [0, 0], "starts": [0, 1]})
    assert not valid_target(target, {"machines": [0, 0], "starts": [0, 0]})
    assert not valid_target(target, {"machines": [0, 0], "starts": [0, 2]})
    assert len(solve_target(target)) == 2
    assert solve_target({**target, "K": 2}) == []
    assert valid_target({**target, "K": 2}, {"no_solution": True})
    assert not valid_target(target, {"no_solution": True})
    yes = no = 0
    for case in cases:
        numbers = case["source"]["numbers"]
        assert all(type(x) is int and x > 0 for x in numbers)
        assert case["expected"] == ({"indices": source_solutions(numbers)[0]}
                                     if source_solutions(numbers) else {"no_solution": True})
        assert valid_source(numbers, case["expected"])
        if source_solutions(numbers):
            yes += 1
        else:
            no += 1
    print(f"self-test passed: {len(cases)} cases ({yes} YES, {no} NO)")


def candidate_test(cases, path):
    yes = no = outputs = alternate = 0
    for case in cases:
        source = case["source"]
        target = run_candidate(path, source)
        schedules = solve_target(target)
        target_outputs = schedules or [{"no_solution": True}]
        assert bool(schedules) == (case["expected"] != {"no_solution": True}), source
        for index, output in enumerate(target_outputs):
            assert valid_target(target, output), (source, output)
            recovered = run_candidate(path, {"source": source, "target_solution": output}, True)
            assert valid_source(source["numbers"], recovered), (source, output, recovered)
            outputs += 1
            alternate += index > 0
        yes += bool(schedules)
        no += not schedules
    print(f"candidate passed: {len(cases)} instances ({yes} YES, {no} NO), {outputs} outputs ({alternate} alternate)")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--self-test", action="store_true")
    group.add_argument("--candidate", type=Path)
    args = parser.parse_args()
    cases = json.loads((WORK / "cases.json").read_text())
    if args.self_test:
        self_test(cases)
    else:
        candidate_test(cases, args.candidate.resolve())


if __name__ == "__main__":
    main()
