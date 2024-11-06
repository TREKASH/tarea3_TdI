# src/rag/data_processing.py

import os
import re

# Directorio donde se almacenan los guiones
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "scripts")

def load_scripts():
    """Carga todos los guiones en la carpeta 'scripts' y los devuelve como una lista de strings."""
    scripts = []
    for filename in os.listdir(SCRIPTS_DIR):
        if filename.endswith(".txt"):
            print(f"Cargando guion: {filename}")  # Imprimir cada archivo cargado
            with open(os.path.join(SCRIPTS_DIR, filename), 'r', encoding='utf-8') as file:
                scripts.append(file.read())
    return scripts

def clean_text(text):
    """Limpia el texto eliminando caracteres especiales, etiquetas HTML y metadatos irrelevantes."""
    # Elimina créditos, metadatos y secuencias no deseadas
    text = re.sub(r'(Screenplay by|Transcription credits|For Your Consideration|Based on .* by|New Line Cinema Presents|Production|Written by|By .*|BLACK SCREEN|FADE IN|CUT TO|INT\.|EXT\.|SUPER|A Wingnut Films|continues|continues\.\.\.|Screenplay|Inc\.|Ltd\.|Hollywood)', '', text, flags=re.IGNORECASE)
    
    # Elimina etiquetas HTML y caracteres especiales no ASCII
    text = re.sub(r'<.*?>', '', text)  # Elimina etiquetas HTML
    text = re.sub(r'[^\x00-\x7F]+', ' ', text)  # Elimina caracteres no ASCII
    # check for ""
    text = re.sub(r'\"', '', text)
    # check for \n
    text = re.sub(r'\n', '', text)
    # check for '
    text = re.sub(r"'", '', text)

    # Elimina múltiples espacios y recorta el texto
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def split_text(text, max_length=1024, min_length=100):
    """Divide el texto en fragmentos manejables y combina fragmentos si son demasiado pequeños."""
    # Dividimos por líneas o escenas (puedes ajustar según el formato de los guiones)
    fragments = text.split("\n\n")  # Divide por párrafos o escenas

    # Crear fragmentos más grandes y combinar si son pequeños
    smaller_fragments = []
    for fragment in fragments:
        # print(f"Fragmento original: {fragment[:30]}...")
        # Dividir fragmento en trozos más grandes si excede el max_length
        while len(fragment) > max_length:
            smaller_fragments.append(fragment[:max_length])
            fragment = fragment[max_length:]
        smaller_fragments.append(fragment)  # Agrega el fragmento restante

    # Combinar fragmentos consecutivos si son menores que min_length
    combined_fragments = []
    temp_fragment = ""
    for fragment in smaller_fragments:
        if len(temp_fragment) + len(fragment) < max_length:
            temp_fragment += " " + fragment
        else:
            if temp_fragment:
                combined_fragments.append(temp_fragment.strip())
            temp_fragment = fragment
    if temp_fragment:
        combined_fragments.append(temp_fragment.strip())
    
    # Elimina fragmentos vacíos
    return [f for f in combined_fragments if len(f) > min_length]
    
def process_scripts():
    """Carga, limpia y fragmenta todos los guiones, y los imprime en la terminal para verificación."""
    processed_fragments = []
    scripts = load_scripts()
    
    for script in scripts:
        clean_script = clean_text(script)
        fragments = split_text(clean_script)
        
        
        processed_fragments.extend(fragments)
    
    return processed_fragments