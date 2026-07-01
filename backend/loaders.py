from pathlib import Path
import pandas as pd
from pypdf import PdfReader
from docx import Document


def cargar_markdown(ruta):
    archivo = Path(ruta)

    return archivo.read_text(
        encoding="utf-8"
    )


def cargar_pdf(ruta):
    texto = ""

    lector = PdfReader(ruta)

    for pagina in lector.pages:
        texto += pagina.extract_text()

    return texto


def cargar_word(ruta):

    documento = Document(ruta)

    texto = ""

    for parrafo in documento.paragraphs:
        texto += parrafo.text + "\n"

    return texto


def cargar_excel(ruta):

    datos = pd.read_excel(ruta)

    return datos.to_string()


def cargar_documento(ruta):

    extension = Path(ruta).suffix.lower()

    if extension == ".md":
        return cargar_markdown(ruta)

    if extension == ".pdf":
        return cargar_pdf(ruta)

    if extension == ".docx":
        return cargar_word(ruta)

    if extension in [".xlsx", ".xls"]:
        return cargar_excel(ruta)


    return "Formato no soportado"


if __name__ == "__main__":

    archivo = (
        "documents/recursos_humanos/"
        "politica_vacaciones.md"
    )

    resultado = cargar_documento(archivo)

    print(resultado)