from backend.retrieval.search import Retriever
from backend.vectorstore.qdrant_manager import QdrantManager

db = QdrantManager()

retriever = Retriever(db)

results = retriever.search(
    "What are the payment terms?"
)

for result in results:

    print("=" * 50)

    print(result.payload["text"])