from google.cloud import vision
import io

def reverse_image(image_path):
    # Initialize the Vision API client
    client = vision.ImageAnnotatorClient()

    # Open the image and read it into memory
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    # Construct an image instance
    image = vision.Image(content=content)

    # Perform label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    # Check if there are errors
    if response.error.message:
        raise Exception(f"Error occurred: {response.error.message}")

    # Extract and print the labels (keywords) related to the image
    result = []
    for label in labels:
        result.append(label.description)

    return result

# Replace with your image path
image_path = "path_to_image.jpg"
results = reverse_image(image_path)

# Display the result
if results:
    print("Related keywords for the image:")
    for item in results:
        print(item)
else:
    print("No results found.")
