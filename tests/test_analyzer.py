from backend.vectorstore.qdrant_manager import QdrantManager
from backend.retrieval.embeddings import EmbeddingModel
from backend.retrieval.search import Retriever
from backend.retrieval.reranker import Reranker
from backend.llm.analyzer import DealAnalyzer
import os

# ---------- CONFIG ----------
api_key = os.getenv("GEMINI_API_KEY")

# ---------- COMPONENTS ----------
db = QdrantManager()

embedder = EmbeddingModel()

retriever = Retriever(
    db,
    embedder
)

reranker = Reranker()

analyzer = DealAnalyzer(api_key)

# ---------- QUERY ----------
query = "What are the payment terms?"

# ---------- RETRIEVE ----------
results = retriever.search(
    query,
    limit=10
)

# ---------- RERANK ----------
best_chunks = reranker.rerank(
    query,
    results,
    top_k=5
)

# ---------- ANALYZE ----------
answer = analyzer.analyze(
    query,
    best_chunks
)

    
print("=" * 60)
print(answer["financial_risk"]["score"])

print()

print(answer["payment_terms"]["summary"])

print()

for flag in answer["red_flags"]:
    print(flag)
print("=" * 60)

db.client.close()