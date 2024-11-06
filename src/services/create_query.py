# src/services/create_query.py

def create_query( vectores: list) -> str:
    """
    Crea un query estructurado para enviar a la API del LLM.
    
    Args:
    - input (str): Consulta del usuario.
    - vectores (list): Lista de fragmentos de texto (contexto) obtenidos mediante RAG.
    
    Returns:
    - str: Prompt estructurado listo para ser enviado a la API.
    """
    # Construimos el contexto a partir de los fragmentos
    context = "\n\n".join(f"[Fragmento {i+1}]\n{fragment}" for i, fragment in enumerate(vectores))
    
    # Construimos el prompt completo
    prompt = f"Contexto de la película:\n{context}"
    

    return prompt

