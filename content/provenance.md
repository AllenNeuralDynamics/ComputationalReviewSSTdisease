(sec-provenance)=
# Pipeline Provenance

This review was produced under the coordinator protocol of the Expert Review Pipeline
(`Expert Review Pipeline v29`, model `claude-opus-5`).
Every number on this page is read from a gate artifact in `provenance/`; none is restated from memory.

## Pipeline Summary

| Quantity | Value | Gate artifact |
|---|---:|---|
| Topic clusters searched | 10 | `gate_scope.json` |
| Sections scoped | 12 | `gate_scope.json` |
| Minimum papers per cluster (floor) | 70 | `gate_scope.json` |
| Structured findings extracted | 844 | `gate_evidence_compliance.json` |
| Unique DOIs | 726 | `gate_evidence_compliance.json` |
| Recorded conflicts | 90 | `gate_evidence_compliance.json` |
| Cross-study figure comparisons | 52 | `gate_evidence_compliance.json` |
| Findings from full text | 461 | `gate_evidence_compliance.json` |
| Findings from abstract only | 383 | `gate_evidence_compliance.json` |
| Full-text rate | 54.6% | `gate_evidence_compliance.json` |
| DOIs mapped to citation keys | 726 | `gate_citation_infrastructure.json` |
| Bibliography entries | 726 | `gate_bibliography.json` |
| Findings curated into section packages | 809 | `gate_evidence_curated.json` |
| Figure comparisons audited | 65 | `gate_figure_audit.json` |
| Figures sent back for redesign or split | 0 | `gate_figure_audit.json` |
| Must-fix critic items outstanding | 0 | `gate_critic_complete.json` |
| Must-fix items on the bookends outstanding | 0 | `gate_bookend_critic.json` |
| Integration passes | ['6a_transition', '6b_crossref', '6c_terminology', '6d_continuity', '6e_figures', '6f_hygiene'] | `gate_integration.json` |
| Figures assembled | 43 | `gate_assembly.json` |
| Runnable notebooks assembled | 43 | `gate_assembly.json` |

## Phase Execution

The pipeline executes 21 phases. Each phase closes with a gate artifact that a separate
validator actor writes or countersigns; the artifacts are kept verbatim in `provenance/`.

| Phase | Gate artifact | Outcome as recorded |
|---|---|---|
| 1 Scope | `gate_scope.json` | scope materialised; review request preserved at `provenance/review_request.md` |
| 2 Evidence gathering | `gate_evidence_compliance.json` | 844 findings over 726 unique DOIs across 10 clusters |
| 3 Citation infrastructure | `gate_citation_infrastructure.json` | 726 DOIs mapped to certified citation keys |
| 4 Section planning | `gate_scaffold_approved.json` | approved; every section planned with at least two figures |
| 5 Evidence curation | `gate_evidence_curated.json` | measured as FAIL on two aggregate checks (see Known limitations) |
| 6 Figure construction and audit | `gate_figure_audit.json` | 65 comparisons audited; 0 redesigns, 0 splits, 61 caveats required |
| 7 Section drafting | `gate_sections_drafted.json` | PASS |
| 8 Blinded section criticism | `gate_critic_complete.json` | 87 must-fix items raised in the first critic round; 0 remaining at close |
| 9 Bibliography | `gate_bibliography.json` | all 726 entries verified against their live CrossRef records |
| 10 Integration | `gate_integration.json` | ['6a_transition', '6b_crossref', '6c_terminology', '6d_continuity', '6e_figures', '6f_hygiene'] passes; 1 dangling cross-reference fixed |
| 11 Introduction and conclusion | `gate_intro_conclusion.json` | both bookends written last from the integrated body, with no new citations |
| 12 Blinded bookend criticism | `gate_bookend_critic.json` | 0 must-fix items remaining after 4 rounds |
| 13 Methods | `pipeline_metrics.json` | Methods rendered from the ledger; snapshot taken at phase 13 |
| 14 Document assembly | `gate_assembly.json` | this repository |

## Known Limitations Carried Forward

The curation gate (`gate_evidence_curated.json`) is recorded as FAIL on two aggregate
checks and was not waived: the per-section packages carry 809 findings against the
Phase 2 total of 844, and sections 1, 3 and 12 retain less than
three-quarters of their declared source-cluster union. Both are losses of breadth
rather than of accuracy — every finding that did reach a section package is traceable
to a database record and carries the verbatim source sentence behind its claim.

383 of 844 findings
(45.4%) were extracted from abstracts rather than full
text, and replication status is unknown for 451 findings
(53.4%). Figures mark abstract-only values
explicitly rather than mixing them silently with full-text values.
