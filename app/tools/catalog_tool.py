import json
import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


class CatalogTool:

    def __init__(self):

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

        with open(
            "app/data/catalog.json",
            "r"
        ) as f:

            self.catalog = json.load(f)

        self.documents = []

        for plan in self.catalog["plans"]:

            text = f"""
            Plan: {plan['name']}
            Price: {plan['price']}
            Features: {', '.join(plan['features'])}
            """

            self.documents.append(text)

        embeddings = self.model.encode(
            self.documents
        )

        self.embedding_matrix = np.array(
            embeddings
        ).astype("float32")

        dimension = self.embedding_matrix.shape[1]

        self.index = faiss.IndexFlatL2(dimension)

        self.index.add(self.embedding_matrix)

    def search_catalog(self, query, top_k=2):

        query_embedding = self.model.encode([query])

        query_embedding = np.array(
            query_embedding
        ).astype("float32")

        distances, indices = self.index.search(
            query_embedding,
            top_k
        )

        results = []

        for idx in indices[0]:
            results.append(self.documents[idx])

        return results