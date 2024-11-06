# src/create_index.py

import os
from rag.data_processing import process_scripts
from rag.embedding_manager import generate_embeddings_for_fragments
from rag.vector_db import VectorDB

def create_index():
    # Nombre del archivo de índice FAISS
    index_file = "vector_index.faiss"
    
    # Inicializar el índice FAISS
    vector_db = VectorDB(embedding_dim=768)

    # Procesar los guiones y generar los fragmentos
    fragments = process_scripts()

    # Generar embeddings para los fragmentos
    embeddings = generate_embeddings_for_fragments(fragments)
    
    # Agregar embeddings al índice y verificar la cantidad de embeddings
    vector_db.add_embeddings(embeddings)
    print(f"Cantidad de embeddings en el índice después de agregar: {vector_db.index.ntotal}")

    # Guardar el índice en archivo
    vector_db.save_index(index_file)
    print(f"Embeddings generados y guardados en {index_file}.")

if __name__ == "__main__":
    create_index()