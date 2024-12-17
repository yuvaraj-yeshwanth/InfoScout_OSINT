from googleapiclient.discovery import build
import base64

def reverse_image(image_path, api_key, cx):
    # Read the image file and convert it to base64 encoding
    with open(image_path, "rb") as image_file:
        image_bytes = base64.b64encode(image_file.read()).decode()

    # Build the Google Custom Search API client
    service = build("customsearch", "v1", developerKey=api_key)
    
    # Perform the search using the base64 image data
    res = service.cse().list(
        q=image_bytes,
        cx=cx,
        searchType="image"
    ).execute()

    # Check if results are returned
    if "items" in res:
        return res["items"]
    else:
        return {"error": "No results found"}

# Replace with your API Key and CSE ID
api_key = "YOUR_API_KEY"
cx = "YOUR_CSE_ID"
image_path = "path_to_image.jpg"

results = reverse_image(image_path, api_key, cx)

print(results)
