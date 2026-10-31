
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class DocumentUploadResponse(BaseModel):
    document_id: str
    filename: str
    file_type: str
    file_size: int
    extracted_text_length: int
    uploaded_at: datetime
    status: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "document_id": "a1b2c3d4-e5f6-7890-abcd-123456789012",
                "filename": "business_report.pdf",
                "file_type": ".pdf",
                "file_size": 245760,
                "extracted_text_length": 12500,
                "uploaded_at": "2026-10-31T10:00:00Z",
                "status": "processed",
            }
        }
    )
