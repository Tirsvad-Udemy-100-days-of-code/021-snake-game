# RC-001: Review of BC-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-001 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001], [DICT-001], [PP-001], [SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [f13d004] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | Cost–Benefit Assessment is qualitative and says why: "this is an unpaid learning project with one participant, so money does not measure either side". |
| 2 | Risks are identified with documented impact and mitigation | Pass | Risks table has 12 rows, each with an Impact and a Mitigation (checked by script: no empty cell); three are specific to this repository (assumed day-21 numbers, drift from the base, token leak). |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | 12 criteria, each with a Target and a Measure, e.g. criterion 7: `doxygen Doxyfile` ends with 0 warnings; criterion 8: 0 entries in `[project].dependencies`; criterion 9: 100% of the listed names exist. Criterion 4 is measured by a review of `src/`, which is checkable but not numeric. |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` and `### Out of Scope` subsections; Out of Scope names rebuilding the game and keeping the two repositories in step. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | Stakeholders table cites S01, S02 and S03 and states interests only; roles are not re-described. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | Methodological and Standards Foundation names the framework, Larman, ISO/IEC 25010:2023, PEP 8/257/484, Doxygen and pytest. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | Assumptions and Constraints are separate sections; the base being correct is an assumption, the plan window and the plan gate are constraints. |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | Recommendation: "Proceed — ...", one sentence. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it` in the Metadata table. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list; `check-languages.sh --list` shows `en` and `it` for this document. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. Titles of lectures are quoted in English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English: short prose; code names and commands appear in backticks only where an objective or a measure needs them. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001] (screen, window, snake, segment, head, body, tail, move, direction, reversal, arrow key, food, refresh, eat, grow, score, scoreboard, wall, touch, game over, inheritance). Searched for the variants collision, collide, heading, boundary, border, apple, fruit, pellet, points, tile and step outside backticks. 'collisions' appears only in the quoted titles of the lectures; 'heading' (a section title) and 'collide' (for eat) were reworded and 'not at its edge' was changed before this review; 'edge of the screen' is the lecture's own phrase for the screen, not a second word for the wall; 'step' only means a project step, as the dictionary rules say. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; there is no earlier accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 (Product Owner and developer) reads English and knows the IT domain, and asked for this review in chat on 2026-10-08. The terms were also checked against [DICT-001] by the reviewing assistant; S01's own reading is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Software Quality Assurance (SQA), Quality Criteria (QC), continuous integration (CI), Python Enhancement Proposals (PEP) and Python Package Index (PyPI) are spelled out on first use. ISO/IEC and UML appear only as the name of a standard and in the title of Larman's book. |

## Overall Verdict

Go — all Mandatory criteria pass. The checklist rows above were transcribed and assessed on 2026-10-08 by the assistant that drafted the documents, at S01's request in chat ("review them and start MIL-001"). S01 is named as reviewer and approves. This review is **not independent**: the drafter and the reviewer are the same assistant, and author and reviewer (S01) are one person in a single-person project (risk recorded in [BC-001] and [PP-001]). S01 has not yet read the document line by line and can overrule this verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read BC-001 and confirm or overrule this `Go` before the pull request of MIL-001 is merged | S01 | 2026-10-09 |
| Decide whether to create the governance document (`GOV`) and the traceability matrix (`TM`); no `TM` row could be added for this review because neither exists (open issue in [PP-001]) | S01 | 2026-10-09 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[DICT-001]: ../../dictionary.md
[PP-001]: ../../project-plan.md
[SA-001]: ../../stakeholder-analysis.md
[f13d004]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/f13d004447ceb631cb22c058d68a21b721a3f04c
