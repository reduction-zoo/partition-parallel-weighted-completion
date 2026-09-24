# Round 001 — equal load through square completion cost

## Plan (2026-09-23, before candidate implementation)

Gap: need an exact target bound and a decoder valid for every feasible schedule, including schedules with idle time and arbitrary job order.

Mechanism: use two machines and jobs whose processing time equals weight, both proportional to each source integer. Within a machine, weighted completion cost should be a quadratic function of its total load plus a source-dependent constant. Test whether an integral `K` can equal the balanced-load lower bound, so any schedule at or below `K` exposes a partition by its machine assignment.

Prior evidence: Prepare's 120 source labels and target solver are fixed at commit `50c5b13`. Search of local and board experience entries for partition, weighted completion, and load balancing found no matching entry; the board collection was empty or absent. The question references the upstream catalog issue but gives no audited construction.

First discriminating check: build a candidate from the exact quadratic identity and run the prepared end-to-end checker on all 120 fixed cases. A mismatch refutes the candidate implementation or mathematical bound on a concrete case; a pass supports only the finite instances and leads to a general proof plus additional verification.

## Evidence and diagnosis

The proposed identity is exact: with `p_i=w_i=2a_i`, any schedule has cost at least `K+(L_0-L_1)^2`, where `K=2Σa_i²+(Σa_i)²`. The proof covers arbitrary job order and idle time. `algorithm.py` constructs the target and decodes every valid schedule by machine membership; target NO-SOLUTION maps to source NO-SOLUTION by the proved equivalence. The candidate's bit lengths and runtime are polynomial, as detailed in [proof](../../work/proof.md).

The prepared Z3 check passed 120 source instances (30 YES, 90 NO) and 150 target outputs (30 alternate valid schedules). [Independent subset-DP verification](../../work/verification.md) passed the same counts with a distinct target solver. No mismatch was observed. This finite result supports implementation behavior; the general claim rests on the algebraic proof.

Literature check on 2026-09-23: [upstream issue #480](https://github.com/CodingThrust/problem-reductions/issues/480) describes `m=2`, `p_i=w_i=a_i` and load balancing, but its bound is truncated/inexact in the visible text and it does not give a complete output decoder. [Lenstra, Rinnooy Kan and Brucker (1977), Theorem 3(b), p. 353](https://ir.cwi.nl/pub/18051/18051A.pdf) give the same construction and exact threshold up to our factor-four scaling. [Shmoys's scheduling notes, Theorem 4.13](https://people.orie.cornell.edu/shmoys/or6335/chapter5.pdf) show the equal processing/weight completion-cost identity in a different single-machine release-date reduction. The mechanism is an executable reconstruction of a published reduction with a positive-integer bound and explicit recovery; it is not a new hardness result.

The [initial independent review](../../reviews/initial/review.md) found a genuine implementation defect: CPython's default decimal-digit cap caused `json.dump` to fail when squaring a legal 8192-bit input. [The retained reproducer](../../reviews/initial/check_large.py) failed with `ValueError` before repair. The arithmetic theorem and 120-case results were unaffected; the all-input executable claim was not. The CLI now disables that cap before both JSON parsing and serialization. This is an implementation repair in the same mechanism, not a new round.

After the repair, the high-bit reproducer and 16384-bit forward/recovery subprocess checks passed. Both 120-instance suites were rerun and again passed 150 target outputs each. The exact command and coverage are in [verification](../../work/verification.md). [Focused independent re-review](../../reviews/followup/review.md) advanced the repaired candidate. The reviewed [Typst paper](../../work/manuscript.pdf) compiled and all three pages were visually inspected on 2026-09-23.

Observation: equal loads are forced by the threshold. Supported cause: the packed cost equals a constant plus the squared load difference, while idle time cannot lower cost. Consequence: no second construction mechanism is needed if independent review accepts the proof.

Experience extraction: [equal processing/weight load-square lemma](../../../../research/experience/equal_processing_weight_load_square.md) created 2026-09-23; applicable beyond this particular source problem. No board file was edited.

## Next action

Round closed supported. Recommend expert review of the complete reconstruction. No construction or proof obligation remains within this campaign; formalization was not requested. One round and one distinct mechanism were used from the 20-round allocation. Further optional optimization is not needed for the fixed acceptance criteria.
