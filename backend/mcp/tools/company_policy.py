class CompanyPolicyTool:

    def run(
        self,
        query
    ):

        policies = {
            "termination": (
                "Company policy requires a 30-day notice "
                "period for contract termination."
            ),

            "confidentiality": (
                "Confidential information must survive "
                "contract termination for 3 years."
            ),

            "payment": (
                "Invoices must be paid within 30 days."
            )
        }

        query = query.lower()

        for keyword, policy in policies.items():

            if keyword in query:

                return policy

        return "No matching company policy found."