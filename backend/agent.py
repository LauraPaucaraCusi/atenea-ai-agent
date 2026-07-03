from backend.vector_store import buscar


def responder(pregunta):

    resultado = buscar(pregunta)

    documentos = resultado["documents"][0]

    metadatos = resultado["metadatas"][0]

    contexto = []

    fuentes = []

    for documento, metadata in zip(documentos, metadatos):

        contexto.append(documento)

        archivo = metadata["archivo"]

        if archivo not in fuentes:
            fuentes.append(archivo)

    respuesta = (
        "Respuesta basada en documentos internos de Soluciones Atenea.\n\n"
    )

    respuesta += "\n\n".join(contexto)

    respuesta += "\n\nFuentes consultadas:\n"

    for fuente in fuentes:

        respuesta += f"- {fuente}\n"

    return respuesta


if __name__ == "__main__":

    print(

        responder(
            "¿Cuándo debo solicitar vacaciones?"
        )

    )