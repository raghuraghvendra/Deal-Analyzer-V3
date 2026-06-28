def build_prompt(query, context):

    return f"""
You are an expert Business Contract Risk Analyst.

Analyze ONLY the provided contract.

User Question:
{query}

Contract Context:
{context}

Return ONLY valid JSON.

Required JSON format:

{{
    "overall_risk": {{
        "score": 0,
        "level": "",
        "summary": ""
    }},

    "financial_risk": {{
        "score": 0,
        "level": "",
        "reason": ""
    }},

    "legal_risk": {{
        "score": 0,
        "level": "",
        "reason": ""
    }},

    "compliance_risk": {{
        "score": 0,
        "level": "",
        "reason": ""
    }},

    "payment_terms": {{
        "summary": "",
        "risk_level": ""
    }},

    "termination_clause": {{
        "present": true,
        "summary": ""
    }},

    "missing_clauses": [],

    "red_flags": [],

    "recommendations": []
}}

Rules:

- Use ONLY the provided contract.
- Never hallucinate.
- If information is unavailable, return "Not Found".
- Scores must be integers between 0 and 10.
- Risk levels must be one of:
  Low
  Medium
  High
- Return ONLY JSON.
"""