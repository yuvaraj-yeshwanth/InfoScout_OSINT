import os
from PIL import Image
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
    Extracts metadata from a variety of files (images, etc.).

    Args:
        file_path (str): Path to the file.
    
    Returns:
        dict: Extracted metadata.
    """
    if not os.path.exists(file_path):
        r
