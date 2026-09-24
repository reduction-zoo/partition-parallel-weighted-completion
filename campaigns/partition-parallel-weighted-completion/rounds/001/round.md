# Round 001 — equal load through square completion cost

## Plan (2026-09-23, before candidate implementation)

Gap: need an exact target bound and a decoder valid for every feasible schedule, including schedules with idle time and arbitrary job order.

Mechanism: use two machines and jobs whose processing time equals weight, both proportional to each source integer. Within a machine, weighted completion cost should be a quadratic function of its total load plus a source-dependent constant. Test whether an integral `K` can equal the balanced-load lower bound, so any schedule at or below `K` exposes a partition by its machine assignment.

Prior evidence: Prepare's 120 source labels and target solver are fixed at commit `50c5b13`. Search of local and board experience entries for partition, weighted completion, and load balancing found no matching entry; the board collection was empty or absent. The question references the upstream catalog issue but gives no audited construction.

First discriminating check: build a candidate from the exact quadratic identity and run the prepared end-to-end checker on all 120 fixed cases. A mismatch refutes the candidate implementation or mathematical bound on a concrete case; a pass supports only the finite instances and leads to a general proof plus additional verification.

## Evidence and diagnosis

Pending.

## Next action

Implement and test the proposed construction and recovery.
