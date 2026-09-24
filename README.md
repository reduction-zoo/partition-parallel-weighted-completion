# Partition → Parallel-machine weighted completion time

**Status:** `ready_for_expert_review` · **Research model:** `gpt-6-sol` · **Submitted:** 2026-09-24

This archive reconstructs a published Partition-to-two-machine weighted-completion reduction as deterministic polynomial-time construction and recovery maps. Every valid target schedule yields a Partition witness; a valid target `NO-SOLUTION` yields source `NO-SOLUTION`. It does not claim a new hardness result.

## Construction

For positive source integers `a_i`, create two machines and one job per integer with processing time and weight `p_i = w_i = 2a_i`. Set `K = 2Σa_i² + (Σa_i)²`. Every schedule costs at least `K` plus the square of the difference between its two source-number loads. A schedule meeting `K` therefore has equal loads, and either machine's jobs give a partition. The decoder uses machine assignments, so arbitrary job order and idle time do not affect recovery.

## Evidence

- **Mathematical correctness and recovery: written proof; independent agent review advanced.** The proof covers all legal inputs and every valid target output, including `NO-SOLUTION`. The reviewer found no remaining correctness gap after a large-integer I/O repair. Human expert acceptance is pending. ([review](campaigns/partition-parallel-weighted-completion/reviews/followup/review.md))
- **Construction and recovery complexity: written polynomial bounds.** The proof gives polynomial runtime and encoding size for both maps. The construction is the published reduction of Lenstra, Rinnooy Kan and Brucker (1977), Theorem 3(b), up to scaling. ([proof](campaigns/partition-parallel-weighted-completion/work/proof.md))
- **Executable verification: finite checks passed.** Z3 and an independent subset-DP solver each checked 120 source instances and 150 valid target outputs, including alternate schedules and no-solution cases. Large-integer recovery checks also passed. These checks supplement, but do not replace, the general proof. ([verification](campaigns/partition-parallel-weighted-completion/work/verification.md))
- **Formal certification and maintainer acceptance: not performed.** No Lean certificate, human expert acceptance, or upstream integration is recorded. ([state](campaigns/partition-parallel-weighted-completion/state.md))

## Reproduce

Run from the repository root:

```sh
uv sync --locked
uv run --locked python campaigns/partition-parallel-weighted-completion/work/check.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py
uv run --locked python campaigns/partition-parallel-weighted-completion/work/verify.py --candidate campaigns/partition-parallel-weighted-completion/work/algorithm.py
uv run --locked python campaigns/partition-parallel-weighted-completion/reviews/initial/check_large.py
```

The finite checks exercise the executable construction and recovery maps. The general claim rests on the written proof.

## Artifacts

- [Fixed question](campaigns/partition-parallel-weighted-completion/question.md)
- [Campaign state](campaigns/partition-parallel-weighted-completion/state.md)
- [Manuscript](campaigns/partition-parallel-weighted-completion/work/manuscript.pdf)
- [Construction and recovery](campaigns/partition-parallel-weighted-completion/work/algorithm.py)
- [General proof](campaigns/partition-parallel-weighted-completion/work/proof.md)
- [Independent review](campaigns/partition-parallel-weighted-completion/reviews/followup/review.md)
- [Verification evidence](campaigns/partition-parallel-weighted-completion/work/verification.md)
