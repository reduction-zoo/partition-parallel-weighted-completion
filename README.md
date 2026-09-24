# Partition → Parallel-machine weighted completion time

Independent research campaign. A published Partition-to-two-machine weighted-completion construction has been reconstructed as executable forward and recovery maps, with a general proof and independent review. The result is ready for expert review; it is not a new hardness classification.

[State](campaigns/partition-parallel-weighted-completion/state.md) · [Question](campaigns/partition-parallel-weighted-completion/question.md) · [Proof](campaigns/partition-parallel-weighted-completion/work/proof.md) · [Paper](campaigns/partition-parallel-weighted-completion/work/manuscript.pdf) · [Independent review](campaigns/partition-parallel-weighted-completion/reviews/followup/review.md)

With source numbers `a_i`, let `S=sum a_i` and `Q=sum a_i²`. Create two machines and jobs with `p_i=w_i=2a_i`; set `K=2Q+S²`. Every schedule costs at least `K+(L_0-L_1)²`, where `L_0,L_1` are the source-number loads on its machines. At or below `K`, machine membership gives a Partition witness. Target `NO-SOLUTION` gives source `NO-SOLUTION`.

Reproduce with Python 3.12, uv 0.12.17, Z3 binding 5.1.0.0 and Typst 0.15.1:

```sh
uv sync --locked
uv run research/validate_preparation.py campaigns/partition-parallel-weighted-completion/work/cases.json
cd campaigns/partition-parallel-weighted-completion/work
uv run check.py --self-test
uv run check.py --candidate algorithm.py
uv run verify.py --candidate algorithm.py
uv run ../reviews/initial/check_large.py
typst compile manuscript.typ manuscript.pdf
```

Both candidate checks passed 120 instances and 150 target outputs each. These finite checks supplement the proof; the [verification record](campaigns/partition-parallel-weighted-completion/work/verification.md) states their limits.

Board source commit: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.
