import os
import magic
from PIL import Image
from PIL.PngImagePlugin import PngImageFile
import fitz  # PyMuPDF
from datetime import datetime

def extract_image_metadata(image_path):
    """
    Extracts metadata from image files (e.g., JPEG, PNG).

    Args:
        image_path (str): Path to the image file.
    
    Returns:
        dict: Extracted metadata.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            metadata = {
                "format": img.format,
                "size": img.size,
                "mode": img.mode,
                "info": img.info
            }

            # Extract EXIF metadata if available (only for formats like JPEG)
            exif_data = img._getexif()
            if exif_data:
                metadata["exif"] = exif_data

            return metadata
    except Exception as e:
        return {"error": f"Could not extract metadata from image: {e}"}

def extract_pdf_metadata(pdf_path):
    """
    Extracts metadata from PDF files.

    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        dict: Extracted metadata.
    """
    try:
        doc = fitz.open(pdf_path)
        metadata = doc.metadata
        # Get document creation and modification dates
        creation_date = doc.metadata.get("creationDate", "Unknown")
        modification_date = doc.metadata.get("modDate", "Unknown")
        metadata["created"] = parse_pdf_date(creation_date)
        metadata["modified"] = parse_pdf_date(modification_date)
        return metadata
    except Exception as e:
        return {"error": f"Could not extract metadata from PDF: {e}"}

def parse_pdf_date(date_str):
    """
    Helper function to parse PDF date format (e.g., D:20240112120000+00'00').

    Args:
        date_str (str): The PDF date string.
    
    Returns:
        str: The parsed date in a readable format.
    """
    try:
        date_str = date_str[2:]  # Remove "D:"
        return datetime.strptime(date_str, "%Y%m%d%H%M%S%z").strftime("%Y-%m-%d %H:%M:%S")
    except Exception:
        return "Invalid date format"

def extract_file_metadata(file_path):
    """
    Extracts general metadata from files including file type, size, and last modified date.

    Args:
        file_path (str): Path to the file.
    
    Returns:
        dict: Basic file metadata.
    """
    try:
        file_metadata = {
            "file_type": magic.from_file(file_path, mime=True),
            "file_size": os.path.getsize(file_path),
            "last_modified": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S"),
            "created": datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H:%M:%S"),
            "path": file_path
        }
        return file_metadata
    except Exception as e:
        return {"error": f"Could not extract file metadata: {e}"}

def extract_metadata(file_path):
    """
    Extracts metadata from a variety of files (images, PDFs, etc.).

    Args:
        file_path (str): Path to the file.
    
    Returns:
        dict: Extracted metadata.
    """
    if not os.path.exists(file_path):
        return {"error": "File does not exist"}

    file_extension = file_path.lower().split('.')[-1]

    # Extract file metadata
    metadata = extract_file_metadata(file_path)

    # Extract specific metadata based on file type
    if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
        image_metadata = extract_image_metadata(file_path)
        metadata.update(image_metadata)
    elif file_extension == 'pdf':
        pdf_metadata = extract_pdf_metadata(file_path)
        metadata.update(pdf_metadata)
    
    return metadata

if __name__ == "__main__":
    # Example usage
    file_path = input("Enter the path of the file to extract metadata: ").strip()
    metadata = extract_metadata(file_path)
    
    if "error" in metadata:
        print(f"Error: {metadata['error']}")
    else:
        print("\nExtracted Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
