from AGENTS.committee_chair_agent import run as chair
from AGENTS.contribution_reviewer_agent import run as contribution
from AGENTS.evidence_examiner_agent import run as evidence
from AGENTS.methodology_critic_agent import run as methodology
from AGENTS.research_question_agent import run as research_question
from safety.policy import authorize


def orchestrate(context: dict) -> dict:
    """Run thesis-review specialists and apply fail-closed academic governance."""
    results = [
        research_question(context),
        methodology(context),
        evidence(context),
        contribution(context),
        chair(context),
    ]
    governance = authorize("committee_support_release", context)
    return {
        "system": "F99",
        "results": results,
        "governance": governance,
        "release_allowed": governance["allowed"],
        "human_review_required": True,
        "autonomous_thesis_decision_authority": False,
        "autonomous_degree_recommendation_authority": False,
    }
