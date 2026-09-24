# Fixed question

```json
{
  "source": "Partition",
  "target": "Parallel-machine weighted completion time",
  "category": "Construction open",
  "summary": "The rule documents the effect of load balancing on total weighted completion time and provides an arithmetic scheduling benchmark.",
  "source_definition": "Given positive binary-encoded integers, return a subcollection with sum equal to half the total. Return NO-SOLUTION exactly when no such witness exists. Graphs, families and strings are explicit; numerical parameters use binary encodings.",
  "target_definition": "Given positive integer processing times and weights, a number of identical machines and K, return a nonpreemptive schedule starting at nonnegative times whose total weighted completion time is at most K. A valid output is a witness satisfying these conditions, or NO-SOLUTION exactly when none exists.",
  "required_result": "Construct deterministic polynomial-time maps F and G. F must produce a legal target instance, and G(x,y) must return a valid source output for every valid target output y, including NO-SOLUTION. A complete rule may reconstruct a published construction or give a new one; it must specify every gadget, numerical parameter and decoding step.",
  "acceptance": "Deliver executable instance construction and output recovery, a general proof covering all legal inputs and target outputs, and worst-case polynomial time and encoding-size bounds. Cite the actual proof used, or identify a newly derived argument. Check small positive and negative instances with independent solvers; finite tests alone do not establish correctness.",
  "importance": "The rule documents the effect of load balancing on total weighted completion time and provides an arithmetic scheduling benchmark.",
  "difficulty": "Difficulty is not yet established by a construction attempt. Derive the exact target bound and use the parallel-machine model. A single-machine precedence model is a different problem.",
  "openness": "This is a rule-completion task from the imported catalog. The requested contribution is a complete, reproducible construction, proof and implementation; the existing hardness attribution is not presented as an unsolved complexity classification. The references are leads to check, not a verified solution.",
  "literature_checked": "2026-09-18",
  "coverage": "Import inventory review of the cited sources. Primary proofs have not been independently re-audited; availability of a complete reconstruction elsewhere remains unassessed.",
  "references": [
    {
      "title": "Problem-Reductions: Partition \u2192 Parallel-machine weighted completion time",
      "url": "https://github.com/CodingThrust/problem-reductions/issues/480",
      "note": "Upstream task and discussion checked on 2026-09-18. Reported reference: Garey & Johnson, *Computers and Intractability*, Appendix A5.2, p.240-241"
    }
  ],
  "solutions": [],
  "equation": ""
}
```
