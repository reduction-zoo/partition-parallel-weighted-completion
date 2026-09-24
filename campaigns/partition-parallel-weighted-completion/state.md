# Campaign state

Budget: 20 rounds. Used: 1. Remaining: 19. Distinct construction mechanisms: 1.
Board source: d56f22aee71c281b1a9b7aa90e65a0d2607efdce.

Capability probe (2026-09-23, local macOS): Python 3.12.14 at `/Users/xiweipan/.local/bin/python3`; uv 0.12.17 at `/Users/xiweipan/.local/bin/uv`; Z3 executable 5.1.0 at `/opt/homebrew/bin/z3` and uv binding `z3-solver==5.1.0.0` selected for Prepare; Kissat 4.0.4 at `/opt/homebrew/bin/kissat`; SCIP 10.1.0 at `/opt/homebrew/bin/scip`; CBC 2.10.13 at `/opt/homebrew/bin/cbc`; Typst 0.15.1 at `/opt/homebrew/bin/typst`; Lean 4.34.0 at `/opt/homebrew/bin/lean`; Lake 5.0.0-src+293d5d0 at `/opt/homebrew/bin/lake`; external writing skill at `/Users/xiweipan/.codex/plugins/cache/sci-brain/sci-brain/0.5.0/skills/how-to-technical-writing/SKILL.md` present. cvc5, MiniSat, CaDiCaL, Glucose and Mathlib: pending. Formalization is not requested.
Prepare: [contract](work/contract.md), [120 fixed cases](work/cases.json), [oracles](work/check.py), and [evidence](work/preparation.md). Corpus gate and self-test passed 2026-09-23. Initial tests cover 30 YES and 90 NO sources, size 1–8. Candidate discovery has not started.
Current claim: complete executable F and G with a general proof in [work/proof.md](work/proof.md). Exact threshold `K=2Σa_i²+(Σa_i)²`; every valid target schedule recovers a balanced subset. Correctness is supported by the proof and finite checks, pending independent review. Novelty: known equal-weight/length load-balancing idea reconstructed with an exact integer bound and decoder; no new hardness classification claimed. Significance: compact one-job-per-number benchmark, pending independent judgment.
Checks: [Prepare](work/preparation.md) passed; [Z3 and independent subset-DP verification](work/verification.md) both passed 120 instances and 150 target outputs. These are finite checks, not general proof.
Experience: 1 [entry](../../research/experience/equal_processing_weight_load_square.md) created, 0 updated, 0 pending.
Next action: fresh independent review of the unchanged round-001 candidate.

| Round | Mechanism / scope | First check | Outcome | Evidence |
|---|---|---|---|---|
| 001 | Equal-load quadratic cost; first construction after Prepare | Fixed 120-case end-to-end suite | Supported | [round](rounds/001/round.md) |
