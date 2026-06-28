from backend.retrieval.embeddings import EmbeddingModel


class Retriever:

    def __init__(
        self,
        qdrant_manager,
        embedder
    ):

        self.db = qdrant_manager
        self.embedder = embedder

    def search(self, query, limit=5):

        query_vector = self.embedder.model.encode(
            query
        ).tolist()

        results = self.db.client.query_points(
            collection_name=self.db.collection_name,
            query=query_vector,
            limit=limit
        )

        return results.points