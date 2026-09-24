# Exact reduction and proof

Let the Partition input be positive integers `a_0,...,a_{n-1}`, with `n >= 1`, total `S`, and square sum `Q = Σ a_i²`. Construct two identical machines. For each `i`, create one job with processing time `p_i = 2a_i` and weight `w_i = 2a_i`. Set `K = 2Q + S²`. All target numbers and `K` are positive integers.

For any feasible nonpreemptive schedule, fix the order of jobs on each machine and shift them left to remove idle time. This weakly decreases every completion time because processing times are positive and starts are nonnegative. Write `L_0` and `L_1` for the sums of the original `a_i` assigned to each machine. The packed schedule's weighted cost on a machine with assigned set `M` is

`Σ_{i∈M} (2a_i)(2 Σ_{j at or before i} a_j) = 2[(Σ_{i∈M} a_i)² + Σ_{i∈M} a_i²]`.

This identity follows by counting each diagonal term `a_i²` twice and each unordered cross term `a_i a_j` twice on both sides. Summing over machines gives packed cost

`2Q + 2(L_0² + L_1²) = 2Q + S² + (L_0-L_1)² = K + (L_0-L_1)²`.

Thus every actual schedule has cost at least `K + (L_0-L_1)²`. If its cost is at most `K`, then `L_0=L_1=S/2`, and the jobs on machine 0 form a Partition witness. This covers arbitrary order and idle time; the decoder reads only machine assignments. Conversely, a Partition witness assigns its jobs to machine 0 and the complement to machine 1. Running both job lists without idle time from zero yields cost exactly `K`, so the target has a valid schedule. Consequently the target has no feasible schedule exactly when the source has no partition. The decoder returns `NO-SOLUTION` on a valid target `NO-SOLUTION` output, and the machine-0 indices on every valid schedule output. Both source outputs satisfy the fixed search contract.

Let `N` be the source bit length. The maps double input numbers, add them, square them and encode `K`; these integer operations use polynomial bit time. Since `S <= n max_i a_i` and `Q <= n max_i a_i²`, the largest target integer has `O(log n + max_i log a_i)` bits and the target has `n` jobs, hence polynomial encoding size. Recovery scans the target output's assignment list in `O(n)` integer inspections plus parsing time polynomial in `N+|y|`. It does not solve Partition or retain data between subprocesses.

The arithmetic proof was derived independently in this campaign, but the reduction is published in [Lenstra, Rinnooy Kan and Brucker (1977), Theorem 3(b), p. 353](https://ir.cwi.nl/pub/18051/18051A.pdf): their `p_i=w_i=a_i` map and threshold become ours after scaling both quantities by two. This campaign supplies an explicit executable output decoder, including NO-SOLUTION, and checks it against independent solvers; it does not claim a new hardness classification. Practical overhead is one job per source integer, two machines, and roughly twice the input number bit length in `K`; no optional optimization is needed. The Python CLI disables CPython's default decimal-digit conversion cap before parsing or emitting JSON integers, so the executable maps cover arbitrary finite positive integers allowed by the bit model.
