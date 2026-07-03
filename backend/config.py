from pathlib import Path

# ===========================
# Rutas
# ===========================

DOCUMENTS_PATH = Path("documents")

DATABASE_PATH = "database"

COLLECTION_NAME = "documentos_atenea"

# ===========================
# Documentos soportados
# ===========================

SUPPORTED_EXTENSIONS = {
    ".md",
    ".txt",
    ".pdf",
    ".docx",
    ".xlsx",
    ".csv",
    ".json",
    ".html"
}

# ===========================
# Configuración RAG
# ===========================

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

TOP_K = 3