
from datetime import datetime, timezone
from pathlib import Path

from fastapi import APIRouter, File, HTTPException, UploadFile

from backend.app.schemas.document import DocumentUploadResponse
from backend.app.services.document_processor import extract_text
from backend.app.services.document_storage import save_document

router = APIRouter(prefix="/documents", tags=["Documents"])


@router.post("/upload", response_model=DocumentUploadResponse)
async def upload_document(file: UploadFile = File(...)):
    saved_document = None

    try:
        saved_document = await save_document(file)

        extracted_text = extract_text(
            saved_document["content"],
            saved_document["file_type"],
        )

        return DocumentUploadResponse(
            document_id=saved_document["document_id"],
            filename=saved_document["filename"],
            file_type=saved_document["file_type"],
            file_size=saved_document["file_size"],
            extracted_text_length=len(extracted_text),
            uploaded_at=datetime.now(timezone.utc),
            status="processed",
        )

    except UnicodeDecodeError:
        raise HTTPException(
            status_code=400,
            detail="TXT files must use UTF-8 encoding.",
        )

    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc))

    except Exception:
        if saved_document:
            Path(saved_document["storage_path"]).unlink(missing_ok=True)

        raise HTTPException(
            status_code=500,
            detail="Unable to process the uploaded document.",
        )

    finally:
        await file.close()
