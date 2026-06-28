COMPLIANCE_RETRIEVAL_PROMPT = """
Find clauses related to:

- GDPR
- Privacy
- Confidentiality
- Compliance
- Security
- Intellectual Property
- Audit Rights
"""


COMPLIANCE_ANALYSIS_PROMPT = """
You are a Senior Compliance Officer.

Analyze ONLY compliance issues.

Return ONLY valid JSON.

{
    "summary": "",
    "risk_score": 0,
    "compliance_issues": [],
    "missing_clauses": [],
    "recommendations": []
}

Do not return markdown.
Return only JSON.
"""