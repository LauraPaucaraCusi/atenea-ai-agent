import chromadb

from backend.loaders import cargar_documento
from backend.chunker import dividir_texto
from backend.utils import (
    obtener_documentos,
    obtener_metadatos
)


cliente = chromadb.PersistentClient(
    path="database"
)

coleccion = cliente.get_or_create_collection(
    name="documentos_atenea"
)


def indexar_documento(ruta):

    print(f"📄 Procesando: {ruta}")

    texto = cargar_documento(ruta)

    fragmentos = dividir_texto(texto)

    metadatos = obtener_metadatos(ruta)

    for i, fragmento in enumerate(fragmentos):

        identificador = f"{ruta}-{i}"

        datos = metadatos.copy()
        datos["chunk"] = i

        coleccion.upsert(
            ids=[identificador],
            documents=[fragmento],
            metadatas=[datos]
        )

        print(f"✅ Guardado: {identificador}")


def indexar_todos():

    documentos = obtener_documentos()

    print()
    print("=" * 50)
    print("INDEXANDO DOCUMENTOS")
    print("=" * 50)

    for documento in documentos:

        indexar_documento(
            str(documento)
        )

    print()
    print("✅ Indexación terminada")


def buscar(pregunta):

    resultado = coleccion.query(
        query_texts=[pregunta],
        n_results=3
    )

    return resultado


if __name__ == "__main__":

    indexar_todos()

    print()
    print("=" * 50)

    resultado = buscar(
        "¿Cuándo debo solicitar vacaciones?"
    )

    print()

    for i in range(len(resultado["documents"][0])):

        print("=" * 50)

        print("📄 Documento:")
        print(resultado["metadatas"][0][i]["archivo"])

        print("📂 Categoría:")
        print(resultado["metadatas"][0][i]["categoria"])

        print("🔹 Chunk:")
        print(resultado["metadatas"][0][i]["chunk"])

        print()
        print(resultado["documents"][0][i])
        print()