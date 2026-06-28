from backend.llm.analyzer import DealAnalyzer


class LLMService:

    def __init__(self, api_key):
        self.model = DealAnalyzer(api_key)

    def generate(self, prompt, context):
        return self.model.analyze(
            prompt,
            context
        )