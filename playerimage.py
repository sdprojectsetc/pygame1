import requests

# URL of the image you want to download
image_url = "https://pnghq.com/wp-content/uploads/plant-png-aesthetic-transparent-image-download-89117-1536x1536.png"  # Replace with your image URL

# Send a GET request to the image URL
response = requests.get(image_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Open the file in binary write mode and save it
    with open("player_image.png", "wb") as file:
        file.write(response.content)
    print("Image downloaded and saved successfully.")
else:
    print("Failed to download the image.")

