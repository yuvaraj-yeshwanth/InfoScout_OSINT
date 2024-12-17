import os
from googleapiclient.discovery import build
from PIL import Image

def reverse_image(image_path, api_key, cx):
    # Open the image and convert it to bytes
    try:
        with open(image_path, "rb") as image_file:
            image_bytes = image_file.read()
    except FileNotFoundError:
        print(f"Error: The image file {image_path} does not exist.")
        return
    
    # Build the Google Custom Search API client
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(
        q=image_bytes,
        cx=cx,
        searchType="image"
    ).execute()

    if "items" in res:
        return res["items"]
    else:
        return {"error": "No results found"}

# Main method to interact with the user
def search_image():
    image_path = input("Enter the path to the image: ")
    api_key = input("Enter your Google API key: ")
    cx = input("Enter your Custom Search Engine ID: ")

    results = reverse_image(image_path, api_key, cx)

    if isinstance(results, list):
        print("Found the following similar images:")
        for item in results:
            print(item['link'])  # Print the link to the similar image
    else:
        print("Error:", results["error"])
