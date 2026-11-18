import os
import secrets

from fastapi import Depends, FastAPI, Header, HTTPException, status
from pydantic import BaseModel, Field

from backend.agent import responder

app = FastAPI(
    title="Atenea AI Agent",
    description="Agente corporativo con RAG",
    version="1.1",
)


class Pregunta(BaseModel):
    pregunta: str = Field(min_length=1, max_length=2000)


def verificar_api_key(x_api_key: str | None = Header(default=None)) -> None:
    """Fail closed: do not serve document searches without configured authentication."""
    expected_key = os.getenv("ATENEA_API_KEY")
    if not expected_key:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="API authentication is not configured",
        )
    if not x_api_key or not secrets.compare_digest(x_api_key, expected_key):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key",
        )


@app.get("/")
def inicio():
    return {"mensaje": "Atenea AI funcionando"}


@app.post("/preguntar", dependencies=[Depends(verificar_api_key)])
def preguntar(datos: Pregunta):
    return {"pregunta": datos.pregunta, "respuesta": responder(datos.pregunta)}
