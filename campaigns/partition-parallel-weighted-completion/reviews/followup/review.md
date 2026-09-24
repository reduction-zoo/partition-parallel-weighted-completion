# Follow-up independent review — 2026-09-23

**Decision: advance to expert review.** I reviewed repair commit `11883dda839756bc8aab1599b4f6f0f3bd124929` against the two findings in [`initial/review.md`](../initial/review.md). The executable large-integer failure is repaired, and the proof now cites the exact published precedent. This is approval for expert review, not a claim of publication acceptance.

## Correctness

The arithmetic rule, decoder, and proof of all valid target schedules and `NO-SOLUTION` outputs are unchanged from the initial review. The load-square identity, legal positive target construction, nonempty answer semantics, deterministic polynomial-time arithmetic, and polynomial output bit length remain sound. The two independent 120-instance injected target-solver loops, their 150 valid outputs including alternate schedules and NO cases, and their limits are unaffected; [`work/verification.md`](../../work/verification.md) reports both reran successfully after repair. I did not repeat those suites.

The changed [`work/algorithm.py`](../../work/algorithm.py) disables CPython's decimal-digit conversion cap at module entry, before line 38 parses either forward or `--extract` JSON and before line 40 serializes `K`. I reran [`initial/check_large.py`](../initial/check_large.py) with `uv run`; it now passes the formerly failing `[2^8192, 2^8192]` case as well as its smaller YES and NO checks. A separate direct subprocess check constructed `[2^16384, 2^16384]`, whose input numerals themselves exceed the old decimal cap, and verified the exact `K=8·(2^16384)^2`, both valid machine assignments through `--extract`, and a neighboring NO case `[2^16384, 2^16384+1]` through `NO-SOLUTION` recovery. It passed. The reviewer-side process disabled its own cap to form and parse these test messages; the candidate was a separate subprocess. The fix therefore covers both directions of JSON conversion without changing the mathematical map or recovery. I found no remaining correctness gap in the current rule.

## Novelty

The initial primary-source search, dated 2026-09-23, remains applicable. [Lenstra, Rinnooy Kan, and Brucker (1977), Theorem 3(b), printed p. 353](https://ir.cwi.nl/pub/18051/18051A.pdf) gives the same Partition-to-two-machine weighted completion construction with `p_i=w_i=a_i`; scaling both by two yields this candidate's map and threshold exactly. [`work/proof.md`](../../work/proof.md) now cites that theorem and describes the campaign's independent derivation without claiming a new hardness classification. The earlier coverage limit remains: I did not audit the Bruno–Coffman–Sethi full text cited by the 1977 paper or exhaustively survey later reproductions. That limit cannot affect the established lack of theorem novelty. The fixed question explicitly accepts a published reconstruction.

## Significance and overhead

The completed contribution is an executable, source-output-preserving reconstruction with an explicit decoder for schedule and NO-SOLUTION outputs, independent small-instance solver checks, and a general proof. It uses one job per source integer, two machines, and target numbers with `O(log n + max_i log a_i)` bits; its `K` roughly doubles input-number bit length. Target solving is still the dominant potentially exponential step. No solver-runtime measurement or speed claim is made. This meets the fixed rule-completion and arithmetic benchmark criteria while adding no new complexity classification.

## Isolation and model route

This follow-up used the registered `research-reviewer` subagent with fresh reviewer context and an inherited GPT-6 model route; no explicit model override was requested, and the exact variant was not exposed here. The actual filesystem profile was `danger-full-access`, approval policy `never`. No tool denial, filesystem sandbox, or enforced depth cap was visible; isolation of writes and delegation depended on the reviewer instructions. I wrote only this file in the assigned follow-up directory, did not alter candidate artifacts, original tests, or earlier evidence, and did not spawn agents. These process boundaries do not themselves establish correctness.
