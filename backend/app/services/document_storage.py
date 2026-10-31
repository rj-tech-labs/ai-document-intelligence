
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from backend.app.core.config import settings


async def save_document(file: UploadFile) -> dict:
    """
    Validate and save an uploaded document.

    Returns document ID, original filename, extension,
    file size and storage path.
    """

    if not file.filename:
        raise ValueError("Filename is required.")

    original_filename = Path(file.filename).name
    extension = Path(original_filename).suffix.lower()

    if extension not in settings.ALLOWED_EXTENSIONS:
        raise ValueError("Only PDF, DOCX and TXT files are supported.")

    file_content = await file.read()

    if not file_content:
        raise ValueError("Uploaded file is empty.")

    max_size = settings.MAX_UPLOAD_SIZE_MB * 1024 * 1024

    if len(file_content) > max_size:
        raise ValueError(
            f"File size exceeds the {settings.MAX_UPLOAD_SIZE_MB} MB limit."
        )

    document_id = str(uuid4())

    upload_directory = Path(settings.UPLOAD_DIR)
    upload_directory.mkdir(parents=True, exist_ok=True)

    storage_path = upload_directory / f"{document_id}{extension}"

    storage_path.write_bytes(file_content)

    return {
        "document_id": document_id,
        "filename": original_filename,
        "file_type": extension,
        "file_size": len(file_content),
        "storage_path": str(storage_path),
        "content": file_content,
    }
