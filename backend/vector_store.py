import chromadb
from pathlib import Path

from backend.loaders import cargar_documento
from backend.chunker import dividir_texto


cliente = chromadb.PersistentClient(
    path="database"
)

coleccion = cliente.get_or_create_collection(
    name="documentos_atenea"
)


def indexar_documento(ruta):

    print(f"📄 Procesando: {ruta}")

    try:

        texto = cargar_documento(ruta)

        fragmentos = dividir_texto(texto)

        for i, fragmento in enumerate(fragmentos):

            coleccion.upsert(
                ids=[f"{ruta}-{i}"],
                documents=[fragmento]
            )

        print(f"✅ {len(fragmentos)} fragmentos indexados")

    except Exception as e:

        print(f"❌ Error leyendo {ruta}")

        print(e)


def indexar_todos():

    carpeta = Path("documents")

    extensiones = [
        ".md",
        ".pdf",
        ".docx",
        ".xlsx",
        ".csv",
        ".json",
        ".html"
    ]

    for archivo in carpeta.rglob("*"):

        if archivo.suffix.lower() in extensiones:

            indexar_documento(
                str(archivo)
            )


def buscar(pregunta):

    return coleccion.query(
        query_texts=[pregunta],
        n_results=2
    )


if __name__ == "__main__":

    indexar_todos()

    respuesta = buscar(
        "¿Cuándo debo solicitar vacaciones?"
    )

    print("\n🔎 Resultado:\n")

    print(respuesta)