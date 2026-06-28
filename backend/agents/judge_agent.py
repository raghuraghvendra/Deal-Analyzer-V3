from backend.agents.base_agent import BaseAgent
from backend.prompts.judge_prompt import (
    JUDGE_SYSTEM_PROMPT
)


class JudgeAgent(BaseAgent):

    def __init__(self, llm_service):

        self.llm = llm_service

    def execute(self, reports):

        final_report = self.llm.generate(
            JUDGE_SYSTEM_PROMPT,
            reports
        )

        return final_report