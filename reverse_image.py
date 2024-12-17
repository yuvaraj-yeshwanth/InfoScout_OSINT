from googleapiclient.discovery import build

def reverse_image(image_path, api_key, cx):
    from PIL import Image
    import io

    # Open the image and convert it to bytes
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

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

# Replace with your API Key and CSE ID
api_key = "YOUR_API_KEY"
cx = "YOUR_CSE_ID"
image_path = "path_to_image.jpg"
results = reverse_image(image_path, api_key, cx)

print(results)
