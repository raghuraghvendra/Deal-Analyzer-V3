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
        print("\nLEGAL REPORT:\n", legal_report)

        financial_report = self.financial.execute()
        print("\nFINANCIAL REPORT:\n", financial_report)

        compliance_report = self.compliance.execute()
        print("\nCOMPLIANCE REPORT:\n", compliance_report)

        reports = {
            "legal": legal_report,
            "financial": financial_report,
            "compliance": compliance_report
        }

        final_report = self.judge.execute(reports)
        print("\nFINAL REPORT:\n", final_report)

        return final_report