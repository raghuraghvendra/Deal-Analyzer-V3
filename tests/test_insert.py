from backend.ingestion.pdf_parser import PDFParser
from backend.ingestion.chunking import Chunker
from backend.retrieval.embeddings import EmbeddingModel
from backend.vectorstore.qdrant_manager import QdrantManager

parser = PDFParser()
chunker = Chunker()
embedder = EmbeddingModel()

text = parser.extract_text("assets/Sample_contract.pdf")

chunks = chunker.create_child_chunks(text)

vectors = embedder.embed_chunks(chunks)

db = QdrantManager()

db.create_collection()

db.insert_chunks(chunks, vectors)

info = db.client.get_collection(
    db.collection_name
)

print("Points Count:", info.points_count)

db.client.close()