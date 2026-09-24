# Prepared testing foundation

Date: 2026-09-23. The fixed corpus in `cases.json` contains 120 distinct sources: 16 hand-designed edge cases and 104 seeded random cases (`generate_cases.py`, seeds 0 onward, skipping duplicate vectors). Size counts: 1:3, 2:18, 3:21, 4:19, 5:15, 6:15, 7:15, 8:14. Exhaustive subset enumeration establishes 30 YES and 90 NO labels. Several YES cases have distinct complementary witnesses.

The source oracle enumerates subsets directly. The target oracle uses Z3 5.1.0.0 through the uv lock. Variables choose each job's machine and nonnegative integer start time. Pairwise disjunctions enforce nonoverlap, and the weighted completion inequality enforces `K`. A satisfying model is exactly an integral schedule under this encoding. Any real-start feasible schedule can be compacted into an integral one without raising completion times, so UNSAT excludes all legal schedules. `unknown` is an error, never NO-SOLUTION. Independent Python predicates check returned schedules and source outputs from the definitions, including incorrect witnesses, overlap, excess cost, and false no-solution answers. For small source cases, stored labels are separately recomputed by `check.py`.

Commands from repository root:

```sh
uv sync --locked
uv run research/validate_preparation.py campaigns/partition-parallel-weighted-completion/work/cases.json
uv run campaigns/partition-parallel-weighted-completion/work/check.py --self-test
```

Both checks passed on 2026-09-23. The corpus gate reported 120 distinct cases, 104 random and 16 edge. The self-test reported 30 YES and 90 NO. The finite corpus reaches eight jobs and values through 20; it cannot establish a general reduction theorem. Candidate testing later runs `uv run campaigns/partition-parallel-weighted-completion/work/check.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py` and independently solves each constructed target instance, including alternate satisfying target outputs where available.
