from backend.agents.base_agent import BaseAgent
from backend.prompts.compliance_prompt import (
    COMPLIANCE_RETRIEVAL_PROMPT,
    COMPLIANCE_ANALYSIS_PROMPT
)


class ComplianceAgent(BaseAgent):

    def __init__(self, llm_service, knowledge_service):

        self.llm = llm_service
        self.knowledge = knowledge_service

    def execute(self):

        context = self.knowledge.retrieve_context(
            COMPLIANCE_RETRIEVAL_PROMPT
        )

        report = self.llm.generate(
            COMPLIANCE_ANALYSIS_PROMPT,
            context
        )

        return report