import os
import tempfile

from backend.agents.orchestrator import AgentOrchestrator
from backend.ingestion.pdf_parser import PDFParser
from backend.ingestion.chunking import Chunker
from backend.retrieval.embeddings import EmbeddingModel
from backend.vectorstore.qdrant_manager import QdrantManager
from backend.services.knowledge_service import KnowledgeService
from backend.llm.llm_service import LLMService


class ContractAnalysisService:

    def __init__(self, api_key):

        self.api_key = api_key

        # Lightweight components only
        self.parser = PDFParser()
        self.chunker = Chunker()

    def analyze(self, uploaded_file):

        # -----------------------------------------
        # Save uploaded PDF temporarily
        # -----------------------------------------
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(uploaded_file.getbuffer())
            pdf_path = temp_file.name

        try:

            # -----------------------------------------
            # Parse PDF
            # -----------------------------------------
            text = self.parser.extract_text(pdf_path)

            if not text or not text.strip():

                raise ValueError(
                    "The uploaded PDF does not contain readable text."
                )

            # -----------------------------------------
            # Chunk Text
            # -----------------------------------------
            chunks = self.chunker.create_child_chunks(text)

            # -----------------------------------------
            # Heavy Components (Lazy Initialization)
            # -----------------------------------------
            embedder = EmbeddingModel()

            db = QdrantManager()
            db.create_collection()

            knowledge_service = KnowledgeService(
                db,
                embedder
            )

            llm = LLMService(
                self.api_key
            )

            orchestrator = AgentOrchestrator(
                llm,
                knowledge_service
            )

            # -----------------------------------------
            # Generate Embeddings
            # -----------------------------------------
            embeddings = embedder.embed_chunks(chunks)

            # -----------------------------------------
            # Store in Qdrant
            # -----------------------------------------
            db.insert_chunks(
                chunks,
                embeddings
            )

            # -----------------------------------------
            # Run Multi-Agent Workflow
            # -----------------------------------------
            answer = orchestrator.execute_workflow()

            return answer

        finally:

            if os.path.exists(pdf_path):
                os.remove(pdf_path)