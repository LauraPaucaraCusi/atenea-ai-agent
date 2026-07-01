from fastapi import FastAPI
from pydantic import BaseModel

from backend.agent import responder


app = FastAPI(
    title="Atenea AI Agent",
    description="Agente corporativo con RAG",
    version="1.0"
)


class Pregunta(BaseModel):
    pregunta: str



@app.get("/")
def inicio():

    return {
        "mensaje": "Atenea AI funcionando"
    }



@app.post("/preguntar")
def preguntar(datos: Pregunta):

    respuesta = responder(
        datos.pregunta
    )

    return {
        "pregunta": datos.pregunta,
        "respuesta": respuesta
    }