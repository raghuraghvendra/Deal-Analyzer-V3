from sentence_transformers import SentenceTransformer


class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(
            "BAAI/bge-small-en-v1.5"
        )

    def embed_chunks(self, chunks):

        embeddings = self.model.encode(
            chunks,
            convert_to_numpy=True
        )

        return embeddings