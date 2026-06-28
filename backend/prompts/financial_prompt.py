FINANCIAL_RETRIEVAL_PROMPT = """
Find clauses related to:

- Payment Terms
- Pricing
- Renewal
- Refunds
- Billing
- Taxes
- Financial Obligations
"""


FINANCIAL_ANALYSIS_PROMPT = """
You are a Senior Financial Contract Analyst.

Analyze ONLY the financial aspects.

Return ONLY valid JSON.

{
    "summary": "",
    "risk_score": 0,
    "payment_summary": "",
    "financial_risks": [],
    "recommendations": []
}

Do not return markdown.
Return only JSON.
"""