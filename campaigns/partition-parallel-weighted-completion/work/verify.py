"""Independent exhaustive scheduling check, separate from the Z3 preparation oracle."""

import argparse
import functools
import itertools
import json
import subprocess
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parent


def source_witnesses(numbers):
    return [set(indices) for count in range(len(numbers) + 1)
            for indices in itertools.combinations(range(len(numbers)), count)
            if 2 * sum(numbers[i] for i in indices) == sum(numbers)]


def schedules(target, limit=2):
    p = target["processing_times"]
    w = target["weights"]
    n = len(p)
    assert n == len(w) and target["machines"] == 2

    @functools.lru_cache(None)
    def best(mask):
        if mask == 0:
            return 0, ()
        elapsed = sum(p[i] for i in range(n) if mask & (1 << i))
        return min((best(mask ^ (1 << last))[0] + w[last] * elapsed,
                    best(mask ^ (1 << last))[1] + (last,))
                   for last in range(n) if mask & (1 << last))

    found = []
    full = (1 << n) - 1
    for mask in range(1 << n):
        left_cost, left_order = best(mask)
        right_cost, right_order = best(full ^ mask)
        if left_cost + right_cost > target["K"]:
            continue
        machine = [0 if mask & (1 << i) else 1 for i in range(n)]
        starts = [0] * n
        for order in (left_order, right_order):
            elapsed = 0
            for i in order:
                starts[i] = elapsed
                elapsed += p[i]
        found.append({"machines": machine, "starts": starts})
        if len(found) == limit:
            break
    return found


def valid_schedule(target, output):
    p, w = target["processing_times"], target["weights"]
    machines, starts = output["machines"], output["starts"]
    n = len(p)
    return (len(machines) == len(starts) == n
            and all(type(m) is int and m in (0, 1) for m in machines)
            and all(type(t) is int and t >= 0 for t in starts)
            and all(machines[i] != machines[j] or starts[i] + p[i] <= starts[j]
                    or starts[j] + p[j] <= starts[i]
                    for i in range(n) for j in range(i + 1, n))
            and sum(w[i] * (starts[i] + p[i]) for i in range(n)) <= target["K"])


def call(path, payload, extract=False):
    result = subprocess.run([sys.executable, str(path)] + (["--extract"] if extract else []),
                            input=json.dumps(payload), capture_output=True, text=True, check=True)
    return json.loads(result.stdout)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--candidate", type=Path, required=True)
    args = parser.parse_args()
    cases = json.loads((WORK / "cases.json").read_text())
    yes = no = outputs = alternate = 0
    for case in cases:
        source = case["source"]
        witnesses = source_witnesses(source["numbers"])
        target = call(args.candidate.resolve(), source)
        target_outputs = schedules(target)
        assert bool(target_outputs) == bool(witnesses), source
        for index, output in enumerate(target_outputs or [{"no_solution": True}]):
            assert output == {"no_solution": True} or valid_schedule(target, output)
            recovered = call(args.candidate.resolve(), {"source": source, "target_solution": output}, True)
            if witnesses:
                assert set(recovered["indices"]) in witnesses, (source, output, recovered)
            else:
                assert recovered == {"no_solution": True}, (source, output, recovered)
            outputs += 1
            alternate += index > 0
        yes += bool(witnesses)
        no += not witnesses
    print(f"verified: {len(cases)} instances ({yes} YES, {no} NO), {outputs} outputs ({alternate} alternate)")


if __name__ == "__main__":
    main()
