from backend.retrieval.search import Retriever
from backend.retrieval.reranker import Reranker
from backend.vectorstore.qdrant_manager import QdrantManager
from backend.retrieval.embeddings import EmbeddingModel

# Connect to Qdrant
db = QdrantManager()

# Create Embedding MOdel
embedder = EmbeddingModel()

# Create Retriever
retriever = Retriever(db, embedder)

# Retrieve top 10 chunks
results = retriever.search(
    "What are the payment terms?",
    limit=10
)

print("=" * 60)
print("BEFORE RERANKING")
print("=" * 60)

for i, result in enumerate(results, start=1):

    print(f"\nRank {i}")
    print(result.payload["text"][:250])

# ----------------------------

reranker = Reranker()

best_chunks = reranker.rerank(
    "What are the payment terms?",
    results,
    top_k=5
)

print("\n")
print("=" * 60)
print("AFTER RERANKING")
print("=" * 60)

for i, result in enumerate(best_chunks, start=1):

    print(f"\nRank {i}")
    print(result.payload["text"][:250])

db.client.close()