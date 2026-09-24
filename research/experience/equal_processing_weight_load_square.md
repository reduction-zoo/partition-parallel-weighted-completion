# Equal processing time and weight turn completion cost into squared loads

Tags: partition, identical parallel machines, weighted completion, quadratic load.

## Claim and applicability

For nonpreemptive identical-machine scheduling with zero release times, positive jobs satisfying `p_i=w_i=c a_i` for one positive integer `c`, the minimum weighted completion cost for a fixed machine assignment is `c²/2 * (Σ_i a_i² + Σ_m L_m²)`, where `L_m` is the sum of `a_i` assigned to machine `m`. Any job order without idle time attains it. Arbitrary idle times only increase the cost. This fails if weights are not proportional to processing times or additional scheduling constraints obstruct compaction.

## Evidence and status

General algebraic lemma proved in [round 001 proof](../../campaigns/partition-parallel-weighted-completion/work/proof.md); independently tested on the campaign's finite corpus in [verification](../../campaigns/partition-parallel-weighted-completion/work/verification.md). The [initial independent review](../../campaigns/partition-parallel-weighted-completion/reviews/initial/review.md) confirmed the mathematical identity and found the same construction in [Lenstra, Rinnooy Kan and Brucker (1977), Theorem 3(b)](https://ir.cwi.nl/pub/18051/18051A.pdf). This entry claims no novelty for the lemma.

## Consequence for search

A tight cost threshold can enforce balanced assignment, and machine membership can decode a source partition. Scale `c=2` when a positive integral threshold is needed for all positive integer inputs.

## Use history

- [Round 001](../../campaigns/partition-parallel-weighted-completion/rounds/001/round.md): derived and used to construct F and G; finite checks passed.
