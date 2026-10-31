
from io import BytesIO

from docx import Document
from pypdf import PdfReader


def extract_text(file_content: bytes, file_extension: str) -> str:
    """
    Extract text from PDF, DOCX or TXT document content.

    Args:
        file_content: Raw document bytes.
        file_extension: File extension (.pdf, .docx or .txt).

    Returns:
        Extracted text as a string.

    Raises:
        ValueError: If the format is unsupported or the document
                    contains no extractable text.
    """

    extension = file_extension.lower()

    if extension == ".txt":
        text = file_content.decode("utf-8-sig")

    elif extension == ".pdf":
        pdf_reader = PdfReader(BytesIO(file_content))

        if pdf_reader.is_encrypted:
            raise ValueError("Password-protected PDF files are not supported.")

        text = "\n".join(
            page.extract_text() or ""
            for page in pdf_reader.pages
        )

    elif extension == ".docx":
        document = Document(BytesIO(file_content))

        text = "\n".join(
            paragraph.text
            for paragraph in document.paragraphs
        )

    else:
        raise ValueError(f"Unsupported document format: {extension}")

    text = text.strip()

    if not text:
        raise ValueError("The document contains no extractable text.")

    return text
