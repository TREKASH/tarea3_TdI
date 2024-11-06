# src/rag/embedding_manager.py

import requests
import json

API_URL = "http://tormenta.ing.puc.cl/api/embed"
MODEL_NAME = "nomic-embed-text"

def generate_embedding(text, retries=3):
    """Genera un embedding para un fragmento de texto utilizando la API, con reintentos en caso de falla."""
    payload = {
        "model": MODEL_NAME,
        "input": text
    }
    headers = {"Content-Type": "application/json"}

    for attempt in range(retries):
        print(f"Intento {attempt + 1} de {retries}")
        try:
            response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
            response.raise_for_status()
            embedding = response.json().get("embeddings", [])
            return embedding[0] if embedding else None
        except requests.RequestException as e:
            print(f"Error generating embedding (intento {attempt + 1}): {e}")
            if attempt == retries - 1:
                return None  # Devolver None si se alcanzaron todos los intentos

def generate_embeddings_for_fragments(fragments):
    """Genera embeddings para una lista de fragmentos y los devuelve en una lista."""
    embeddings = []
    for fragment in fragments:
        embedding = generate_embedding(fragment)
        if embedding:
            embeddings.append(embedding)
        else:
            print(f"Failed to generate embedding for fragment: {fragment[:30]}...")

    # Imprimir el total de embeddings generados vs. total de fragmentos
    print(f"Total de embeddings generados: {len(embeddings)} / {len(fragments)}")
    return embeddings