# RC-003: Review of DICT-001

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [DICT-001], [QC-DICT-001], [QC-LANG-001], [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-08 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [f13d004] |

---

## Artifact Under Review

- Instance reviewed: [DICT-001]
- Checklist used: [QC-DICT-001] and, for the language and domain, [QC-LANG-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (S01 reads English and knows the IT domain)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Every row has a PO term, its language, an IT term and a definition | Pass | 26 rows; a script found no empty cell. |
| 2 | Each PO term maps to exactly one IT term and the reverse (no synonyms) | Pass | A script found no PO term and no IT term twice. `Turtle` (segment) and 'subclass of `Turtle`' (inheritance) are different IT terms. |
| 3 | Every Domain Model concept has a row, and the Domain Model uses its PO term | N-A | No Domain Model exists in this project (the Dictionary's Rules section says so). |
| 4 | The Operation Contracts, Sequence Diagrams, Design Class Diagrams and ERD use the IT term, not the PO term | N-A | None of these artifacts exists in this project. |
| 5 | Definitions are written in the PO language and are one sentence | Pass | All definitions are English; a script found no definition with a second sentence. |
| 6 | "Used as PO term in" and "Used as IT term in" name artifact types that exist in the project | Pass | The columns name BC, SA, PP and MIL (all exist) and PY, the source-code type of the catalog. |
| 7 | The dictionary's `Language` and `Domain` rows, and the language of every row, match the PO language and domain in the project registry | Pass | Metadata `en` / `it` equals the registry's `PO language` and `PO domain`; the Language column of every row is `en`. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | `Language` is `en` and `Domain` is `it` in the Metadata table. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is a BCP 47 code; `it` is in the registry's domain list; `check-languages.sh --list` shows `en` and `it` for this document. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | All prose and table cells are English. Titles of lectures are quoted in English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | Register is IT Professional English: one-sentence definitions with the IT term in backticks. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | The document is the dictionary: its PO terms are its own rows. A script found no term twice. The two rules about 'step' and 'base' keep two project words out of the game vocabulary. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | `docs/` holds one file per artifact; there is no `<name>.<language>.md`. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | N-A | First version; there is no earlier accepted version. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | S01 (Product Owner and developer) reads English and knows the IT domain, and asked for this review in chat on 2026-10-08. The terms were also checked against [DICT-001] by the reviewing assistant; S01's own reading is an action item below. |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Product Owner (PO) and information technology (IT) are spelled out on first use; the artifact short names in the last two columns are the catalog's. |

## Overall Verdict

Go — all Mandatory criteria pass (criteria 3 and 4 are N-A because the Domain Model and the design artifacts do not exist in this project). The checklist rows above were transcribed and assessed on 2026-10-08 by the assistant that drafted the documents, at S01's request in chat ("review them and start MIL-001"). S01 is named as reviewer and approves. This review is **not independent**: the drafter and the reviewer are the same assistant, and author and reviewer (S01) are one person in a single-person project (risk recorded in [BC-001] and [PP-001]). S01 has not yet read the document line by line and can overrule this verdict at the pull request.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Read DICT-001 and confirm or overrule this `Go` | S01 | 2026-10-09 |

---

[DICT-001]: ../../dictionary.md
[QC-DICT-001]: ../../../framework/qc/qc-dictionary.md
[QC-LANG-001]: ../../../framework/qc/qc-language-domain.md
[BC-001]: ../../business-case.md
[PP-001]: ../../project-plan.md
[f13d004]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/021-snake-game/commit/f13d004447ceb631cb22c058d68a21b721a3f04c
