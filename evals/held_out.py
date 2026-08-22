from orchestration.orchestrator import orchestrate


def base():
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


SCENARIOS = [
    ({}, False),
    (base(), True),
    ({**base(), "human_committee_approval": False}, False),
    ({**base(), "research_question_gap": True}, False),
    ({**base(), "methodology_validity_gap": True}, False),
    ({**base(), "evidence_provenance_missing": True}, False),
    ({**base(), "unsupported_contribution_claim": True}, False),
    ({**base(), "research_integrity_concern": True}, False),
    ({**base(), "conflict_of_interest_unresolved": True}, False),
    ({**base(), "due_process_gap": True}, False),
]


def main():
    passed = 0
    for context, expected in SCENARIOS:
        passed += orchestrate(context)["release_allowed"] is expected
    print(f"held-out: {passed}/{len(SCENARIOS)} passed")
    raise SystemExit(0 if passed == len(SCENARIOS) else 1)


if __name__ == "__main__":
    main()
