from backend.agents.base_agent import BaseAgent
from backend.agents.tool_decision import ToolDecisionEngine
from backend.mcp.client import MCPClient
from backend.mcp.server import MCPServer
from backend.prompts.legal_prompt import (
    LEGAL_RETRIEVAL_PROMPT,
    LEGAL_ANALYSIS_PROMPT
)


class LegalAgent(BaseAgent):

    def __init__(self, llm_service, knowledge_service):

        self.llm = llm_service
        self.knowledge = knowledge_service

        self.mcp = MCPClient(
            MCPServer()
        )
        
        self.tool_decision = ToolDecisionEngine()

    def execute(self):

        context = self.knowledge.retrieve_context(
            LEGAL_RETRIEVAL_PROMPT
        )

        policy = ""

        if self.tool_decision.should_use_company_policy(
            LEGAL_RETRIEVAL_PROMPT
        ):

            policy = self.mcp.use_tool(
                "company_policy",
                query=LEGAL_RETRIEVAL_PROMPT
            )

        analysis_data = {
            "retrieved_context": context,
            "tool_results": {
            "company_policy": policy
            }
        }

        report = self.llm.generate(
            LEGAL_ANALYSIS_PROMPT,
            analysis_data
        )
 




        return report