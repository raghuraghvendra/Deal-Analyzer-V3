from backend.agents.legal_agent import LegalAgent
from backend.agents.financial_agent import FinancialAgent
from backend.agents.compliance_agent import ComplianceAgent
from backend.agents.judge_agent import JudgeAgent


class AgentOrchestrator:

    def __init__(
        self,
        llm_service,
        knowledge_service
    ):

        self.legal = LegalAgent(
            llm_service,
            knowledge_service
        )

        self.financial = FinancialAgent(
            llm_service,
            knowledge_service
        )

        self.compliance = ComplianceAgent(
            llm_service,
            knowledge_service
        )

        self.judge = JudgeAgent(
            llm_service
        )

    def execute_workflow(self):

        legal_report = self.legal.execute()

        financial_report = self.financial.execute()

        compliance_report = self.compliance.execute()

        reports = {
            "legal": legal_report,
            "financial": financial_report,
            "compliance": compliance_report
        }

        return self.judge.execute(reports)