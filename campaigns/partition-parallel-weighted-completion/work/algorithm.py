"""Partition to two-machine weighted completion feasibility, with recovery."""

import json
import sys


def numbers_from(source):
    numbers = source["numbers"]
    if not isinstance(numbers, list) or not numbers or any(type(a) is not int or a <= 0 for a in numbers):
        raise ValueError("numbers must be a nonempty list of positive integers")
    return numbers


def forward(source):
    numbers = numbers_from(source)
    return {
        "processing_times": [2 * a for a in numbers],
        "weights": [2 * a for a in numbers],
        "machines": 2,
        "K": 2 * sum(a * a for a in numbers) + sum(numbers) ** 2,
    }


def extract(source, target_solution):
    numbers = numbers_from(source)
    if target_solution == {"no_solution": True}:
        return {"no_solution": True}
    machines = target_solution["machines"]
    if len(machines) != len(numbers) or any(type(m) is not int or m not in (0, 1) for m in machines):
        raise ValueError("invalid machine assignment")
    return {"indices": [i for i, machine in enumerate(machines) if machine == 0]}


if __name__ == "__main__":
    payload = json.load(sys.stdin)
    output = extract(payload["source"], payload["target_solution"]) if sys.argv[1:] == ["--extract"] else forward(payload)
    json.dump(output, sys.stdout)
    sys.stdout.write("\n")
