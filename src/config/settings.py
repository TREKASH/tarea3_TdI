# settings.py
from dotenv import load_dotenv

load_dotenv()

class GlobalConfig:
    def __init__(self):
        pass

    # Configuraciones generales de la API
    title: str = "FastAPI Base"
    version: str = "1.0.0"
    description: str = "API Base example"
    openapi_prefix: str = ""
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    openapi_url: str = "/openapi.json"

    # Prefijo para los endpoints
    api_prefix: str = "/api"

    # Configuración de CORS
    allow_origins: list[str] = ["*"]  # Permite todos los orígenes (ajustar en producción)
    allow_methods: list[str] = ["*"]  # Permite todos los métodos HTTP
    allow_headers: list[str] = ["*"]  # Permite todos los headers

# Instancia de configuración global
settings = GlobalConfig()