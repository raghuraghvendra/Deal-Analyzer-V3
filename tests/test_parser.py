from backend.retrieval.search import Retriever
from backend.vectorstore.qdrant_manager import QdrantManager
from backend.retrieval.embeddings import EmbeddingModel

db = QdrantManager()
embedder = EmbeddingModel()

retriever = Retriever(db, embedder)

results = retriever.search(
    "What are the payment terms?"
)

for result in results:

    print("=" * 50)

    print(result.payload["text"])