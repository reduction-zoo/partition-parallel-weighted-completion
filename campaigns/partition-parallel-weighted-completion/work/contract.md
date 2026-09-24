# Executable contract

Source input is `{"numbers": [a_0, ..., a_{n-1}]}`, with `n >= 1` and each `a_i` a positive integer. Integers use JSON decimal syntax and are interpreted as arbitrary-precision binary-encoded values for complexity bounds. A source output is `{"indices": [i_1, ..., i_k]}` with distinct in-range indices summing to half the total, or `{"no_solution": true}` exactly when no such subset exists.

Target input is `{"processing_times": [p_0, ..., p_{q-1}], "weights": [w_0, ..., w_{q-1}], "machines": m, "K": K}` with `q,m >= 1`, positive integral `p_j,w_j`, and nonnegative integral `K`. Target output is `{"machines": [b_0, ..., b_{q-1}], "starts": [s_0, ..., s_{q-1}]}` with integral machine indices in `[0,m)`, nonnegative integer start times, no overlapping intervals on the same machine, and `sum_j w_j(s_j+p_j) <= K`; or `{"no_solution": true}` iff none exists. Integer schedules suffice for existence because processing times are integral and any feasible schedule can be left-justified on each machine.

`algorithm.py` reads one source JSON object from stdin and writes one target JSON object to stdout. `algorithm.py --extract` reads `{"source": ..., "target_solution": ...}` and writes one source output. Both modes are independent processes; errors exit nonzero. Candidate implementation is deliberately absent from Prepare.
