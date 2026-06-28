from backend.retrieval.search import Retriever
from backend.retrieval.reranker import Reranker


class KnowledgeService:

    def __init__(self, db, embedder):
        self.retriever = Retriever(db, embedder)
        self.reranker = Reranker()

    def retrieve_context(self, query, limit=10, top_k=5):

        results = self.retriever.search(
            query,
            limit=limit
        )

        context = self.reranker.rerank(
            query,
            results,
            top_k=top_k
        )

        return context