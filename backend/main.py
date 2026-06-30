from fastapi import FastAPI

app = FastAPI(
    title="Atenea AI Agent",
    description="Agente corporativo con RAG",
    version="1.0"
)


@app.get("/")
def inicio():
    return {
        "mensaje": "Atenea AI funcionando"
    }