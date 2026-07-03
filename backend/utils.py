from pathlib import Path

from backend.config import SUPPORTED_EXTENSIONS


def obtener_documentos():

    carpeta = Path("documents")

    documentos = []

    for archivo in carpeta.rglob("*"):

        if archivo.suffix.lower() in SUPPORTED_EXTENSIONS:

            documentos.append(archivo)

    return documentos


def obtener_metadatos(ruta):

    ruta = Path(ruta)

    return {
        "archivo": ruta.name,
        "ruta": str(ruta),
        "categoria": ruta.parent.name,
        "extension": ruta.suffix.lower()
    }