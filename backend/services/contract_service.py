import os
import tempfile

from backend.agents.orchestrator import AgentOrchestrator
from backend.ingestion.pdf_parser import PDFParser
from backend.ingestion.chunking import Chunker
from backend.retrieval.embeddings import EmbeddingModel
from backend.vectorstore.qdrant_manager import QdrantManager
from backend.services.knowledge_service import KnowledgeService
from backend.llm.llm_service import LLMService
#from backend.agents.orchestrator import AgentOrchestrator
from backend.agents.legal_agent import LegalAgent
from backend.agents.financial_agent import FinancialAgent
from backend.agents.compliance_agent import ComplianceAgent

class ContractAnalysisService:

    def __init__(self, api_key):

        # Core Components
        self.parser = PDFParser()
        self.chunker = Chunker()
        self.embedder = EmbeddingModel()

        # Vector Database
        self.db = QdrantManager()
        self.db.create_collection()

        # Retrieval
        self.knowledge_service = KnowledgeService(
            self.db,
            self.embedder
        )

        # LLM
        self.llm = LLMService(api_key)

        self.orchestrator = AgentOrchestrator(
            self.llm,
            self.knowledge_service
        )

    def analyze(self, uploaded_file):

        # -----------------------------
        # Save uploaded PDF temporarily
        # -----------------------------
        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        ) as temp_file:

            temp_file.write(uploaded_file.getbuffer())
            pdf_path = temp_file.name

        try:

            # -----------------------------
            # Parse PDF
            # -----------------------------
            text = self.parser.extract_text(pdf_path)

            # -----------------------------
            # Chunk Text
            # -----------------------------
            chunks = self.chunker.create_child_chunks(text)

            # -----------------------------
            # Generate Embeddings
            # -----------------------------
            embeddings = self.embedder.embed_chunks(chunks)

            # -----------------------------
            # Store in Qdrant
            # -----------------------------
            self.db.insert_chunks(
                chunks,
                embeddings
            )


            # -----------------------------
            # LLM Analysis
            # -----------------------------
           
            ###best_chunks = self.knowledge_service.retrieve_context(
              ###  "Analyze this contract"
            ###)

            answer = self.orchestrator.execute_workflow()

            ##answer = self.llm.generate(
              ##  "Analyze this contract",
               ## best_chunks
            ##)

            return answer

        finally:

            # Delete temporary PDF
            if os.path.exists(pdf_path):
                os.remove(pdf_path)