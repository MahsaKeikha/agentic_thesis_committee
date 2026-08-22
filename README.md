# F99 | Agentic Thesis Committee | L3 Gold Standard | v1.0

A governed multi-agent reference system for thesis and dissertation committee support, including research-question review, methodology critique, evidence examination, contribution assessment, research-integrity review, and committee preparation.

## Five-agent architecture

- Research Question Agent
- Methodology Critic
- Evidence Examiner
- Contribution Reviewer
- Committee Chair Agent

## Gold-standard academic governance

F99 is fail closed and advisory only. Committee-support release requires reviewed research questions, methodology, evidence, contribution claims, research integrity, conflicts of interest, due process, and explicit qualified-human committee approval.

Release is blocked for unclear research scope, unresolved methodological-validity gaps, incomplete evidence provenance, unsupported originality or contribution claims, research-integrity concerns, unresolved committee conflicts of interest, due-process gaps, or unresolved conflicting evidence.

The reference system cannot autonomously make a thesis or defense decision, recommend a degree, make an academic-integrity finding, change student records, or submit externally. Final academic judgments remain solely with authorized faculty and the institution.

## Verification gates

CI runs on Python 3.10, 3.11, and 3.12 and requires:

```bash
ruff check . --select E9,F63,F7,F82
python -m pytest -q
python evals/held_out.py
python run.py
```

The behavioral verification layer includes eight direct governance tests and a 10-scenario held-out thesis-governance suite.
