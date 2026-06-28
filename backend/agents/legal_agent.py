from backend.agents.base_agent import BaseAgent
from backend.prompts.legal_prompt import (
    LEGAL_RETRIEVAL_PROMPT,
    LEGAL_ANALYSIS_PROMPT
)


class LegalAgent(BaseAgent):

    def __init__(self, llm_service, knowledge_service):

        self.llm = llm_service
        self.knowledge = knowledge_service

    def execute(self):

        context = self.knowledge.retrieve_context(
            LEGAL_RETRIEVAL_PROMPT
        )

        report = self.llm.generate(
            LEGAL_ANALYSIS_PROMPT,
            context
        )

        return report