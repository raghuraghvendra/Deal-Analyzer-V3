from google import genai
import json
from backend.prompts.analyzer_prompt import build_prompt


class DealAnalyzer:

    def __init__(self, api_key):

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = "gemini-2.5-flash"

    def analyze(
        self,
        prompt,
        context
    ):

        # If context comes from Qdrant (list of chunks)
        if isinstance(context, list):

            final_context = ""

            for chunk in context:
                final_context += chunk.payload["text"] + "\n\n"

            prompt = build_prompt(
                prompt,
                final_context
            )

        # If context is already a dictionary/string
        else:

            prompt = f"""
{prompt}

Context:

{json.dumps(context, indent=2)}
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        cleaned = response.text.replace("```json", "")
        cleaned = cleaned.replace("```", "").strip()

        return json.loads(cleaned)