from backend.retrieval.search import Retriever
from backend.vectorstore.qdrant_manager import QdrantManager
from backend.retrieval.embeddings import EmbeddingModel

print("Step 1")

db = QdrantManager()
embedder = EmbeddingModel()

print("Step 2")

retriever = Retriever(db, embedder)

print("Step 3")

results = retriever.search(
    "What are the payment terms?"
)

print("Step 4")

print("Results count:", len(results))

for result in results:
    print("=" * 50)
    print(result.score)
    print(result.payload["text"][:300])

db.client.close()

print("Step 5")