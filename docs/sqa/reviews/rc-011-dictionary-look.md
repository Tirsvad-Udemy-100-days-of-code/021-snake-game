# RC-011: Re-review of DICT-001 (snake look)

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001], [RC-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Proposed | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | [b53be04] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review. Two definitions changed and a row was added, so a delta re-review is not allowed. Earlier record: [RC-003].
- Reason: The segment is no longer one white square, the head has the mouth, and "mouth" is a new game term.
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`; the assistant also drafted the change)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | All 27 rows have a PO term, `en`, an IT term and a definition. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | Each PO term has one IT term and no IT term is used twice; the new `MOUTH_OUTLINE` (mouth) is distinct from `head`, `segments` and `segments[1:]`. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists in this project. |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | No Operation Contract, Sequence Diagram, Design Class Diagram or ERD exists in this project. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | Every definition, including the two changed ones and the new one, is one sentence in English. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | Rows name `BC`, `SA`, `PP`, `MIL` and `PY`; Python source code exists in `src/snake_game/`. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | `Language | en` and `Domain | it` match the registry; every row is `en`. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it` in Metadata. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English, including the new and changed text and the Version History row. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Professional English: precise terms and IDs, no business padding. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms are those of [DICT-001], including the new row `mouth`; `light green` and `dark green` are the names of Tk colours, written as such in backticks where they are values and in plain words elsewhere. `screenshot` is the word of S01's request and is used for the one file `docs/images/snake-score-5.png`; it is not a game term and has no dictionary row. A search for 'white square', 'mouth' used for anything but the wedge, and 'picture' used for the screenshot found none. This document is the dictionary; the other documents were checked against it. |
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
| Read [DICT-001] and confirm or overrule this `Go` when accepting the plan | S01 | 2026-10-13 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/artifacts/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/artifacts/qc-language-domain.md
[RC-003]: ./rc-003-dictionary.md
[b53be04]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/b53be043c2ed2ff35aec4399154826769b8cdf39
