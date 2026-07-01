from backend.vector_store import buscar



def responder(pregunta):

    resultado = buscar(
        pregunta
    )


    documentos = resultado["documents"][0]


    contexto = "\n".join(
        documentos
    )


    respuesta = f"""
Respuesta basada en documentos internos:

{contexto}
"""


    return respuesta



if __name__ == "__main__":

    print(
        responder(
            "¿Cuándo debo solicitar vacaciones?"
        )
    )