import chromadb

from backend.loaders import cargar_documento
from backend.chunker import dividir_texto


cliente = chromadb.PersistentClient(
    path="database"
)


coleccion = cliente.get_or_create_collection(
    name="documentos_atenea"
)



def indexar_documento(ruta):

    print("📄 Procesando:", ruta)

    texto = cargar_documento(ruta)

    fragmentos = dividir_texto(texto)


    for i, fragmento in enumerate(fragmentos):

        identificador = f"{ruta}-{i}"


        coleccion.upsert(
            documents=[fragmento],
            ids=[identificador]
        )


        print(
            "✅ Guardado:",
            identificador
        )



def buscar(pregunta):

    resultado = coleccion.query(
        query_texts=[pregunta],
        n_results=2
    )

    return resultado



if __name__ == "__main__":

    archivo = (
        "documents/recursos_humanos/"
        "politica_vacaciones.md"
    )


    indexar_documento(
        archivo
    )


    respuesta = buscar(
        "¿Cuándo debo solicitar vacaciones?"
    )


    print(respuesta)