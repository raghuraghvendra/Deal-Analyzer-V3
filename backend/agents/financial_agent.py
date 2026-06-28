from backend.agents.base_agent import BaseAgent
from backend.prompts.financial_prompt import (
    FINANCIAL_RETRIEVAL_PROMPT,
    FINANCIAL_ANALYSIS_PROMPT
)


class FinancialAgent(BaseAgent):

    def __init__(self, llm_service, knowledge_service):

        self.llm = llm_service
        self.knowledge = knowledge_service

    def execute(self):

        context = self.knowledge.retrieve_context(
            FINANCIAL_RETRIEVAL_PROMPT
        )

        report = self.llm.generate(
            FINANCIAL_ANALYSIS_PROMPT,
            context
        )

        return report