from AGENTS.research_question_agent import run as a
from AGENTS.methodology_critic_agent import run as b
from AGENTS.evidence_examiner_agent import run as c
from AGENTS.contribution_reviewer_agent import run as d
from AGENTS.committee_chair_agent import run as e
def orchestrate(context): return [a(context),b(context),c(context),d(context),e(context)]
