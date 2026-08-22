from orchestration.orchestrator import orchestrate
from safety.policy import authorize


def valid_context():
    return {
        "research_question_reviewed": True,
        "methodology_reviewed": True,
        "evidence_reviewed": True,
        "contribution_reviewed": True,
        "research_integrity_reviewed": True,
        "conflict_of_interest_reviewed": True,
        "due_process_reviewed": True,
        "human_committee_approval": True,
    }


def test_complete_review_can_release_committee_support():
    result = orchestrate(valid_context())
    assert result["release_allowed"] is True
    assert result["autonomous_thesis_decision_authority"] is False


def test_missing_committee_approval_fails_closed():
    context = valid_context()
    context["human_committee_approval"] = False
    assert orchestrate(context)["release_allowed"] is False


def test_thesis_decision_is_never_autonomous():
    assert authorize("thesis_decision", valid_context())["allowed"] is False


def test_methodology_gap_blocks_release():
    context = valid_context()
    context["methodology_validity_gap"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_missing_evidence_provenance_blocks_release():
    context = valid_context()
    context["evidence_provenance_missing"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_unsupported_contribution_blocks_release():
    context = valid_context()
    context["unsupported_contribution_claim"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_conflict_of_interest_blocks_release():
    context = valid_context()
    context["conflict_of_interest_unresolved"] = True
    assert orchestrate(context)["release_allowed"] is False


def test_due_process_gap_blocks_release():
    context = valid_context()
    context["due_process_gap"] = True
    assert orchestrate(context)["release_allowed"] is False
