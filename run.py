from orchestration.orchestrator import orchestrate

REFERENCE_CONTEXT = {
    "thesis_context": "committee review support",
    "research_question_reviewed": True,
    "methodology_reviewed": True,
    "evidence_reviewed": True,
    "contribution_reviewed": True,
    "research_integrity_reviewed": True,
    "conflict_of_interest_reviewed": True,
    "due_process_reviewed": True,
    "human_committee_approval": True,
}

if __name__ == "__main__":
    print(orchestrate(REFERENCE_CONTEXT))
