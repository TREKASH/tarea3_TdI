import requests
import json

def send_query_to_llm(prompt: str, context: str) -> str:
    """
    Envía un prompt a la API del LLM y devuelve la respuesta generada.
    
    Args:
    - prompt (str): El prompt estructurado para enviar al modelo LLM.
    
    Returns:
    - str: Respuesta generada por el LLM.
    """
    url = "http://tormenta.ing.puc.cl/api/generate"  # URL de la API del LLM
    full_prompt = f"considering the following context: {context}, answer the following question: {prompt}"

    data = {
        "model": "integra-LLM",
        "prompt": full_prompt,
        "stream": False  # Para recibir la respuesta completa en una sola respuesta
    }
    print(data)


    try:
        # Realiza la solicitud POST con el payload JSON
        response = requests.post(url, json=data, headers={'Content-Type': 'application/json'}, timeout=120)
        response.raise_for_status()  # Lanza una excepción para códigos de error HTTP 4xx o 5xx
        
        # Procesa la respuesta JSON
        result = response.json()
        return result.get("response", "No se recibió respuesta del modelo.")
    
    except requests.exceptions.RequestException as e:
        return f"Error en la solicitud a la API del LLM: {e}"