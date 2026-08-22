"""Fail-closed academic governance for F99 Thesis Committee."""

PROTECTED_ACTIONS = {
    "thesis_decision",
    "degree_recommendation",
    "student_record_change",
    "external_submission",
    "defense_outcome",
    "academic_integrity_finding",
}

REQUIRED_REVIEWS = (
    "research_question_reviewed",
    "methodology_reviewed",
    "evidence_reviewed",
    "contribution_reviewed",
    "research_integrity_reviewed",
    "conflict_of_interest_reviewed",
    "due_process_reviewed",
    "human_committee_approval",
)


def authorize(action: str, context: dict | None = None) -> dict:
    context = context or {}
    if action in PROTECTED_ACTIONS:
        return {"allowed": False, "reason": "binding thesis authority is outside reference-system scope"}

    missing = [key for key in REQUIRED_REVIEWS if not context.get(key)]
    if missing:
        return {"allowed": False, "reason": "missing required thesis review", "missing": missing}

    blockers = []
    if context.get("research_question_gap"):
        blockers.append("research question or scope remains materially unclear")
    if context.get("methodology_validity_gap"):
        blockers.append("methodological validity gap unresolved")
    if context.get("evidence_provenance_missing"):
        blockers.append("evidence provenance or traceability incomplete")
    if context.get("unsupported_contribution_claim"):
        blockers.append("original contribution is overclaimed or unsupported")
    if context.get("research_integrity_concern"):
        blockers.append("research-integrity concern requires human adjudication")
    if context.get("conflict_of_interest_unresolved"):
        blockers.append("committee conflict of interest unresolved")
    if context.get("due_process_gap"):
        blockers.append("student due-process or response opportunity incomplete")
    if context.get("conflicting_evidence_unresolved"):
        blockers.append("material conflicting evidence remains unresolved")

    if blockers:
        return {"allowed": False, "reason": "thesis-review governance blocker", "blockers": blockers}

    return {"allowed": True, "reason": "committee-support package approved after qualified human review"}


def review_required(action: str) -> bool:
    return action in PROTECTED_ACTIONS


def enforce(action: str, approved: bool) -> None:
    if review_required(action) and not approved:
        raise PermissionError("Qualified human approval is required for this action.")
