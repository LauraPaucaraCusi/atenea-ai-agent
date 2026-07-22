# Atenea AI Agent

## Descripción

Atenea AI Agent es un agente inteligente desarrollado como parte del Challenge de Alura + Oracle Next Education.

El proyecto implementa una arquitectura **RAG (Retrieval-Augmented Generation)** para responder preguntas utilizando únicamente la información contenida en documentos internos de una empresa.

La solución procesa documentos, los indexa mediante ChromaDB y permite consultar esa información a través de una API desarrollada con FastAPI.

---

# Objetivos

* Centralizar la documentación interna.
* Facilitar la búsqueda de información.
* Reducir los tiempos de consulta.
* Evitar respuestas inventadas utilizando recuperación basada en documentos.

---

# Arquitectura

Usuario

↓

FastAPI

↓

Agente (agent.py)

↓

Búsqueda Vectorial (ChromaDB)

↓

Documentos Indexados

↓

Respuesta

---

# Tecnologías utilizadas

* Python 3
* FastAPI
* ChromaDB
* LangChain
* Uvicorn
* Pandas
* OpenPyXL
* Python-docx
* PyPDF

---

# Estructura del proyecto

```text
atenea-ai-agent/

backend/
    agent.py
    vector_store.py
    loaders.py
    chunker.py
    utils.py
    config.py
    main.py

documents/
    comercial/
    financiero/
    legal/
    operaciones/
    recursos_humanos/
    tecnologia/

database/

README.md
requirements.txt
```

---

# Flujo del sistema

1. Cargar documentos.
2. Extraer el contenido.
3. Dividir el texto en fragmentos (Chunks).
4. Generar metadatos.
5. Indexar en ChromaDB.
6. Recibir preguntas mediante FastAPI.
7. Buscar documentos relacionados.
8. Mostrar la respuesta.

---

# Ejemplos de preguntas

* ¿Cuándo debo solicitar vacaciones?
* ¿Qué beneficios tienen los colaboradores?
* ¿Cuál es la política de compras?
* ¿Cómo funciona el protocolo de emergencias?
* ¿Cuál es la política de privacidad?

---

# Ejemplo de respuesta

Pregunta:

¿Cuándo debo solicitar vacaciones?

Respuesta:

El agente identifica el documento **politica_vacaciones.md** y responde que las vacaciones deben solicitarse con al menos **15 días de anticipación**, indicando además el documento y la categoría desde donde obtuvo la información.

---

# Cómo ejecutar el proyecto

Crear el entorno virtual:

```bash
python -m venv venv
```

Activar el entorno:

Windows

```bash
venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Indexar documentos:

```bash
python -m backend.vector_store
```

Ejecutar la API:

```bash
uvicorn backend.main:app --reload
```

Abrir la documentación:

```text
http://127.0.0.1:8000/docs
```

---

# Resultado

El agente responde consultas utilizando únicamente la información almacenada en los documentos indexados, devolviendo además la fuente de donde obtuvo la información.

---

# Autor

Laura Daniela Paucara Cusi

Ingeniera en Metalurgia

Challenge Alura + Oracle Next Education
