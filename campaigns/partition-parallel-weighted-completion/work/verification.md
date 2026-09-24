# Independent executable verification

Candidate: `work/algorithm.py` and `work/proof.md` from round 001, tested 2026-09-23 against the fixed corpus at Prepare commit `50c5b13`.

Run from repository root:

```sh
uv sync --locked
uv run campaigns/partition-parallel-weighted-completion/work/check.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py
uv run campaigns/partition-parallel-weighted-completion/work/verify.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py
```

Both commands passed: 120 source instances (30 YES, 90 NO), 150 valid target outputs (30 alternate schedules). The first solver uses Z3 integer scheduling constraints. The second uses an independently implemented exact subset dynamic program for minimum weighted completion time on each machine, enumerates two-machine assignments, constructs feasible schedules, and rechecks their objective and overlap. Both run F and G as separate subprocesses. Thus the recovery checks include alternate valid target assignments and the explicit no-solution output. All numerical comparisons are exact integers.

The tests cover 1–8 jobs and source values up to 20. They do not establish the general theorem or test large binary integers. The general proof is in `proof.md`. Solver runtime was not measured as an efficiency claim.
