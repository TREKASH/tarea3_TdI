from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings
from src.routes.index import router as index_router

# Crear la aplicación FastAPI con configuraciones de settings
app = FastAPI(
    title=settings.title,
    version=settings.version,
    description=settings.description,
    openapi_prefix=settings.openapi_prefix,
    docs_url=settings.docs_url,
    redoc_url=settings.redoc_url,
    openapi_url=settings.openapi_url
)

# Configuración de CORS usando los valores de settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origins,  # Lista de orígenes permitidos
    allow_credentials=True,                # Permitir el uso de credenciales
    allow_methods=settings.allow_methods,   # Métodos HTTP permitidos
    allow_headers=settings.allow_headers    # Headers permitidos
)

# Incluir el router principal con el prefijo "/api"
app.include_router(index_router, prefix=settings.api_prefix)

# Ruta de prueba en la raíz
@app.get("/")
async def root():
    return {"Say": "Hello!"}