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

        # -------------------------------------------------
        # Case 1 : Specialist Agents (RAG + MCP)
        # -------------------------------------------------
        if (
            isinstance(context, dict)
            and "retrieved_context" in context
        ):

            final_context = ""

            retrieved_chunks = context.get(
                "retrieved_context",
                []
            )

            for chunk in retrieved_chunks:

                final_context += (
                    chunk.payload["text"] + "\n\n"
                )

            tool_results = context.get(
                "tool_results",
                {}
            )

            if tool_results:

                final_context += (
                    "\n\n===== TOOL RESULTS =====\n"
                )

                for tool_name, result in tool_results.items():

                    if result:

                        final_context += (
                            f"\n{tool_name}:\n{result}\n"
                        )

            prompt = build_prompt(
                prompt,
                final_context
            )

        # -------------------------------------------------
        # Case 2 : Old RAG Pipeline
        # -------------------------------------------------
        elif isinstance(context, list):

            final_context = ""

            for chunk in context:

                final_context += (
                    chunk.payload["text"] + "\n\n"
                )

            prompt = build_prompt(
                prompt,
                final_context
            )

        # -------------------------------------------------
        # Case 3 : Judge Agent
        # -------------------------------------------------
        else:

            prompt = f"""
{prompt}

Specialist Reports:

{json.dumps(context, indent=2)}

Combine these reports into one final enterprise analysis.

Return ONLY valid JSON.
"""

        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )

        cleaned = response.text.replace(
            "```json",
            ""
        )

        cleaned = cleaned.replace(
            "```",
            ""
        ).strip()

        try:

            return json.loads(cleaned)

        except json.JSONDecodeError:

            return {
                "error": True,
                "message": "The AI returned an invalid JSON response.",
                "raw_response": cleaned
            }