# RC-009: Re-review of BC-001 (snake look and screenshot)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-009 |
| CrossReference | [BC-001], [QC-BC-001], [QC-LANG-001], [RC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b53be04] |

---

## Artifact Under Review

- Instance reviewed: [BC-001]
- Checklist used: [QC-BC-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. Two objectives, two success criteria, scope items, risks, assumptions, a constraint, the costs and the recommendation changed, so a delta re-review is not allowed. Earlier record: [RC-001].
- Reason: S01 asked on 2026-10-13 for a light green body and a dark green head with a mouth, which departs from the white squares of the lectures (objective 11), and for a real screenshot of the game in the README and on the wiki (objective 12).
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also drafted the change)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | ROI/Cost-Benefit analysis is quantitative, or where qualitative, is explicitly justified | Pass | Cost–Benefit Assessment is still qualitative and justified; the cost is now about one week and two days and the benefit covers objectives 1 to 12. |
| 2 | Risks are identified with documented impact and mitigation | Pass | Risks table has 15 rows, each with an Impact and a Mitigation; the three new rows cover the compound head shape (colours fixed inside it, `turtle` needed at import time, tests with a fake `turtle` module that has `Shape`), a screenshot that goes out of date, and a screenshot that needs a real window. |
| 3 | Success criteria are measurable, stating explicit targets rather than vague aspirations | Pass | Success Criteria has 14 rows with a Target and a Measure; row 13 states observable targets (segments behind the head light green, head dark green with a mouth at its front that turns with it, a gained segment light green, food blue, text white) and row 14 an observable file, README and wiki page, both naming the Go/No-Go list of [MIL-004]. |
| 4 | Scope explicitly separates In Scope vs Out of Scope | Pass | `### In Scope` has the look of the snake and the screenshot; `### Out of Scope` names animating the mouth and a capture tool in the repository. |
| 5 | Stakeholders are cross-referenced to Stakeholder Analysis IDs rather than re-described inline | Pass | Stakeholders table cites S01, S02 and S03 and states interests only; objective numbers are extended to 12 for S01 and S03. |
| 6 | Methodology and quality-standard foundation are stated explicitly (e.g. ISO/IEC 25010, Larman) | Pass | Methodological and Standards Foundation is unchanged except that `mouth` joins the domain terms. |
| 7 | Assumptions and constraints are explicit and clearly distinguished from one another | Pass | The two new assumptions (the greens and the mouth; the empty wiki) are in Assumptions and the autonomous-mode note is in Constraints; the plan window is unchanged. |
| 8 | Document supports executive decision-making with a clear, unambiguous recommendation | Pass | Recommendation: "Proceed — ...", one sentence, updated for the look, the screenshot and the extra two days. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new and changed text and the Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Executive English; code names and commands appear in backticks only where a target or a check needs them. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001], including the new row `mouth`; `light green` and `dark green` are the names of Tk colours, written as such in backticks where they are values and in plain words elsewhere. `screenshot` is the word of S01's request and is used for the one file `docs/images/snake-score-5.png`; it is not a game term and has no dictionary row. A search for 'white square', 'mouth' used for anything but the wedge, and 'picture' used for the screenshot found none. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | Language and domain are unchanged since the previous accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | The assistant, as stand-in for S01, reads English and knows the IT domain and checked the terms against [DICT-001]. S01's own reading of the changed text is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | No new abbreviation is introduced; the ones already in use stay spelled out on first use. |

## Overall Verdict

Go — all Mandatory criteria pass or are not applicable. The rows above were assessed on 2026-10-13 by the assistant that drafted the change, as stand-in for S01 in autonomous mode (chosen by S01 in chat on 2026-10-13). Mode: autonomous, not independent. This review is **not independent**: the drafter and the reviewer are the same assistant, and author and approver (S01) are one person in a single-person project. S01 can overrule this verdict when accepting the plan and at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Accept the plan in chat, which also confirms or replaces the assumed greens and the mouth of [MIL-004] | S01 | 2026-10-13 |
| Challenge this `Go` in the run summary or on the pull request of MIL-004 if the stand-in decision is not wanted | S01 | 2026-10-15 |

---

[BC-001]: ../../business-case.md
[QC-BC-001]: ../../../framework/qc/artifacts/qc-business-case.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[RC-001]: ./rc-001-business-case.md
[MIL-004]: ../../milestones/mil-004-snake-look-and-screenshot.md
[DICT-001]: ../../dictionary.md
[b53be04]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/b53be043c2ed2ff35aec4399154826769b8cdf39
