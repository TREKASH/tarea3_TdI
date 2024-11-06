# src/query_index.py

import os
from src.services.create_query import create_query
from src.rag.vector_db import VectorDB
from src.rag.data_processing import process_scripts  # Para acceder a los fragmentos
from src.rag.retrival import retrieve_information
from src.services.send_query import send_query_to_llm
def query_index(input: str):
    # Nombre del archivo de índice FAISS
    index_file = "vector_index.faiss"
    
    # Verificar que el archivo de índice existe antes de cargar
    if not os.path.exists(index_file):
        print(f"Error: No se encontró el archivo de índice '{index_file}'. Ejecute 'create_index.py' para crear el índice.")
        return
    
    # Inicializar el índice FAISS y cargar desde archivo
    vector_db = VectorDB(embedding_dim=768)
    vector_db.load_index(index_file)
    print(f"Índice cargado desde {index_file} con {vector_db.index.ntotal} embeddings.")
    
    # Procesar los guiones para obtener los fragmentos (necesarios para mostrar los resultados de la consulta)
    fragments = process_scripts()

    # Pedir una consulta al usuario
    query = input
    vectores = retrieve_information(query, vector_db, fragments)
    prompt = create_query(vectores)
    respuesta = send_query_to_llm(query, prompt)

    return(respuesta)

