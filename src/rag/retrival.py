# src/rag/retrival.py

from src.rag.embedding_manager import generate_embeddings_for_fragments

def retrieve_information(query, vector_db, fragments, k=3):
    """Recupera fragmentos similares a la consulta proporcionada."""
    # Generar el embedding para la consulta
    query_embedding = generate_embeddings_for_fragments([query])[0]
    
    # Buscar los fragmentos más similares en el índice
    indices, distances = vector_db.search_similar(query_embedding, k=k)

    # Mostrar los fragmentos más similares
    print("\nFragmentos más similares encontrados:")
    vectores = []
    for idx, distance in zip(indices, distances):
        
        # print(f"index: {idx}")
        # print(f"Fragmento similar: {fragments[idx]}")
        # print(f"Distancia: {distance}\n")
        vectores.append(fragments[idx])
    
    return vectores
