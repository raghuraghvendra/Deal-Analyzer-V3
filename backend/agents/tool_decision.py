class ToolDecisionEngine:

    def should_use_company_policy(
        self,
        query
    ):

        keywords = [
            "policy",
            "termination",
            "confidentiality",
            "payment",
            "compliance"
        ]

        query = query.lower()

        return any(
            keyword in query
            for keyword in keywords
        )