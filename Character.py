import os
import requests
from PIL import Image
import io

class Character:
    # Constructor to initialize character attributes
    def __init__(self, name, gender, species, origin, status, image, number_of_episodes):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.image_url = image
        self.number_of_episodes = number_of_episodes
        
        # names for downloaded images
        # Creates a file path by replacing spaces in the name with '_'
        self.image_path = './images/' + self.name.replace(' ', '_') + '.png'
        
        # Automatically downloads the image when the object is created
        self.download_image()

    # Method to download the character image
    def download_image(self):
        # Check if the file does not exist, then download the image
        if not os.path.exists(self.image_path):
            # Check if the base directory exists and create it if not
            os.makedirs(os.path.dirname(self.image_path), exist_ok=True)
            
            # Download the image content
            response = requests.get(self.image_url)
            img_data = response.content
            
            # Open image from binary data using PIL
            image = Image.open(io.BytesIO(img_data))
            
            # resizing the image
            # Note: Image.ANTIALIAS is deprecated in modern PIL versions, 
            # replaced by Image.Resampling.LANCZOS or Image.LANCZOS.
            # Assuming older version based on the code style.
            resized_image = image.resize((200, 200), Image.ANTIALIAS)
            
            # Save the resized image locally
            resized_image.save(self.image_path)
            
            print(f'{self.name} Image is Downloaded!') # Use f-string for clarity

    # Method to retrieve the image for display in the GUI
    def get_image(self):
        # Returns an opened PIL Image object from the local path
        return Image.open(self.image_path)