from backend.vector_store import buscar


def responder(pregunta):

    resultado = buscar(pregunta)

    documentos = resultado["documents"][0]
    metadatos = resultado["metadatas"][0]

    respuesta = []

    respuesta.append("=" * 60)
    respuesta.append("ATENEA AI")
    respuesta.append("=" * 60)
    respuesta.append("")
    respuesta.append(f"Pregunta: {pregunta}")
    respuesta.append("")
    respuesta.append(
        f"Se encontraron {len(documentos)} documentos relacionados."
    )
    respuesta.append("")

    for documento, metadata in zip(documentos, metadatos):

        respuesta.append("-" * 60)

        respuesta.append(
            f"Documento : {metadata['archivo']}"
        )

        respuesta.append(
            f"Categoría : {metadata['categoria']}"
        )

        respuesta.append(
            f"Chunk      : {metadata['chunk']}"
        )

        respuesta.append("")
        respuesta.append("Contenido encontrado:")
        respuesta.append("")
        respuesta.append(documento)
        respuesta.append("")

    respuesta.append("=" * 60)

    return "\n".join(respuesta)


if __name__ == "__main__":

    print(
        responder(
            "¿Cuándo debo solicitar vacaciones?"
        )
    )