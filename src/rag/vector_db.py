# src/rag/vector_db.py

import faiss
import numpy as np

class VectorDB:
    def __init__(self, embedding_dim=768, index_file=None):
        """Inicializa la base de datos vectorial utilizando FAISS."""
        self.embedding_dim = embedding_dim
        self.index = faiss.IndexFlatL2(embedding_dim)
        
        # Cargar índice desde archivo si se proporciona uno
        if index_file:
            self.load_index(index_file)

    def add_embeddings(self, embeddings):
        """Agrega una lista de embeddings al índice."""
        embeddings_array = np.array(embeddings).astype('float32')
        self.index.add(embeddings_array)

    def search_similar(self, query_embedding, k=5):
        """Busca los k embeddings más similares al query_embedding."""
        query_embedding = np.array([query_embedding]).astype('float32')
        distances, indices = self.index.search(query_embedding, k)
        return indices[0], distances[0]

    def save_index(self, file_path="vector_index.faiss"):
        """Guarda el índice en un archivo."""
        faiss.write_index(self.index, file_path)
        print(f"Índice guardado en {file_path}")

    def load_index(self, file_path):
        """Carga el índice desde un archivo."""
        self.index = faiss.read_index(file_path)
        print(f"Índice cargado desde {file_path}")

