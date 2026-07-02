from pathlib import Path
from pypdf import PdfReader
from docx import Document
import pandas as pd
import json


def cargar_documento(ruta):

    ruta = Path(ruta)

    extension = ruta.suffix.lower()


    if extension == ".md":

        return ruta.read_text(
            encoding="utf-8"
        )


    elif extension == ".txt":

        return ruta.read_text(
            encoding="utf-8"
        )


    elif extension == ".pdf":

        lector = PdfReader(ruta)

        texto = ""

        for pagina in lector.pages:

            contenido = pagina.extract_text()

            if contenido:
                texto += contenido + "\n"

        return texto


    elif extension == ".docx":

        documento = Document(ruta)

        texto = ""

        for parrafo in documento.paragraphs:

            texto += parrafo.text + "\n"

        return texto


    elif extension == ".xlsx":

        excel = pd.read_excel(
            ruta
        )

        return excel.to_string(index=False)


    elif extension == ".csv":

        csv = pd.read_csv(
            ruta
        )

        return csv.to_string(index=False)


    elif extension == ".json":

        with open(
            ruta,
            encoding="utf-8"
        ) as archivo:

            datos = json.load(archivo)

        return json.dumps(
            datos,
            indent=2,
            ensure_ascii=False
        )


    elif extension == ".html":

        return ruta.read_text(
            encoding="utf-8"
        )


    else:

        raise Exception(
            f"Formato no soportado: {extension}"
        )