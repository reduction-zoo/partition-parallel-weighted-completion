# Independent executable verification

Candidate: `work/algorithm.py` and `work/proof.md` from round 001, tested 2026-09-23 against the fixed corpus at Prepare commit `50c5b13`.

Run from repository root:

```sh
uv sync --locked
uv run campaigns/partition-parallel-weighted-completion/work/check.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py
uv run campaigns/partition-parallel-weighted-completion/work/verify.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py
```

Both commands passed: 120 source instances (30 YES, 90 NO), 150 valid target outputs (30 alternate schedules). The first solver uses Z3 integer scheduling constraints. The second uses an independently implemented exact subset dynamic program for minimum weighted completion time on each machine, enumerates two-machine assignments, constructs feasible schedules, and rechecks their objective and overlap. Both run F and G as separate subprocesses. Thus the recovery checks include alternate valid target assignments and the explicit no-solution output. All numerical comparisons are exact integers.

The tests cover 1–8 jobs and source values up to 20. They do not establish the general theorem. The general proof is in `proof.md`. Solver runtime was not measured as an efficiency claim.

The initial reviewer found an executable failure at CPython's decimal-digit cap. Its [retained high-bit check](../reviews/initial/check_large.py) failed on the pre-repair candidate and passed after the CLI disabled the cap before JSON I/O. A direct subprocess check also passed a 16384-bit source integer through forward parsing, bound serialization and `--extract` parsing (2026-09-23). Both 120-instance suites were rerun and passed after this repair, each again covering 150 outputs. These checks address the specific bit-size failure; they do not replace the general polynomial-time analysis.
