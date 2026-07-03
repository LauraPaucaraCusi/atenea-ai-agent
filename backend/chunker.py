from backend.config import (
    CHUNK_SIZE,
    CHUNK_OVERLAP
)


def dividir_texto(
    texto,
    tamaño=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP
):

    fragmentos = []

    inicio = 0

    while inicio < len(texto):

        fin = inicio + tamaño

        fragmentos.append(
            texto[inicio:fin]
        )

        inicio += tamaño - overlap

    return fragmentos


if __name__ == "__main__":

    texto = """
    Soluciones Atenea tiene una política de vacaciones.
    Los colaboradores deben solicitar vacaciones con anticipación.
    Recursos Humanos revisa las solicitudes.
    """

    partes = dividir_texto(texto)

    for numero, parte in enumerate(partes):

        print(f"\n----- CHUNK {numero} -----\n")

        print(parte)