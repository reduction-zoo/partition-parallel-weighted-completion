"""Fixed, reproducible source corpus; no candidate construction here."""

import itertools
import json
import random
from pathlib import Path


EDGE = [
    [1], [2], [3], [1, 1], [1, 2], [2, 2], [1, 1, 1], [1, 2, 3],
    [2, 3, 5], [1, 1, 2], [1, 1, 1, 1], [2, 2, 2, 2],
    [1, 3, 3, 5], [4, 4, 4], [5, 5, 10], [1, 1, 1, 3],
]


def source_answer(numbers):
    total = sum(numbers)
    for size in range(len(numbers) + 1):
        for indices in itertools.combinations(range(len(numbers)), size):
            if 2 * sum(numbers[i] for i in indices) == total:
                return {"indices": list(indices)}
    return {"no_solution": True}


def main():
    cases = []
    seen = set()

    def add(numbers, kind, seed=None):
        key = tuple(numbers)
        if key in seen:
            return
        seen.add(key)
        case = {"source": {"numbers": numbers}, "kind": kind, "expected": source_answer(numbers)}
        if seed is not None:
            case["seed"] = seed
        cases.append(case)

    for numbers in EDGE:
        add(numbers, "edge")
    for seed in range(1000):
        if sum(c["kind"] == "random" for c in cases) >= 104:
            break
        rng = random.Random(seed)
        add([rng.randint(1, 20) for _ in range(2 + seed % 7)], "random", seed)
    path = Path(__file__).with_name("cases.json")
    path.write_text(json.dumps(cases, indent=2) + "\n")
    print(f"wrote {len(cases)} cases to {path}")


if __name__ == "__main__":
    main()
