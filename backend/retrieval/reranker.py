from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):

        self.model = CrossEncoder(
            "cross-encoder/ms-marco-MiniLM-L-6-v2"
        )

    def rerank(self, query, results, top_k=5):

        pairs = []

        for result in results:

            pairs.append(
                (
                    query,
                    result.payload["text"]
                )
            )

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(results, scores),
            key=lambda x: x[1],
            reverse=True
        )

        best_chunks = []

        for result, score in ranked[:top_k]:
            best_chunks.append(result)

        return best_chunks