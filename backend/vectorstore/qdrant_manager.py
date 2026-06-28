from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct

class QdrantManager:

    def __init__(self):

        self.client = QdrantClient(
            path="./qdrant_data"
        )

        self.collection_name = "contracts"

    def create_collection(self):

        collections = self.client.get_collections()

        existing = [
            col.name
            for col in collections.collections
        ]

        if self.collection_name not in existing:

            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

            print("Collection created")

        else:
            print("Collection already exists")


            

    def insert_chunks(self, chunks, embeddings):
        points = []

        for idx, (chunk, vector) in enumerate(
            zip(chunks, embeddings)
        ):

            points.append(
                PointStruct(
                    id=idx,
                    vector=vector.tolist(),
                    payload={
                        "text": chunk
                    }
                )
            )
        

        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )

        print(f"Inserted {len(points)} chunks")