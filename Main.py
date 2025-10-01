# Import modules 
from tkinter import * 
import requests
from Character import Character
from PIL import Image, ImageTk

from Scrollable import ScrollableFrame

def load_data():
    characters = []
    # Base URL for the first page of the character API
    url = 'https://rickandmortyapi.com/api/character/?page=1'
    
    # Make the GET request to the API
    response = requests.get(url)
    
    # Parse the JSON response
    json_response = response.json()
    
    # Get the list of characters from the 'results' key
    json_characters = json_response['results']

    # Loop through each character object in the results
    for obj in json_characters:
        # Create a new Character object, extracting and transforming data
        character = Character(
            obj['name'], 
            obj['gender'], 
            obj['species'],
            obj['origin']['name'], 
            obj['status'], 
            obj['image'],
            len(obj['episode']) # Count of episodes the character appeared in
        )
        # Add the created object to the list
        characters.append(character)

    # Return the list of Character objects
    return characters

# Load the data 
characters = load_data()

# Get the first character as a sample data 
character = characters[0]

# Create the UI 
root = Tk()
root.title("Rick and Morty")
root.geometry("535x560")
root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
root.resizable(0, 0)
scrollable = ScrollableFrame(root)

list_row = 0 # Initialize row counter

for character in characters:
    # ------------------ Image 687086.png Content (Left Frame) ------------------
    # Frame for each list item
    list_item_frame = Frame(master=scrollable.scrollable_frame, borderwidth=4, relief=GROOVE)

    # Left frame (for the image)
    left_frame = Frame(master=list_item_frame)
    image = ImageTk.PhotoImage(character.get_image())
    image_lbl = Label(left_frame, image=image)
    image_lbl.image = image # Keep reference
    image_lbl.pack(fill=BOTH, expand=True)
    left_frame.grid(row=0, column=0, padx=7.5, pady=15)
    
    # ------------------ Image 6870c6.jpg Content (Right Frame) ------------------
    # Right frame (for text details)
    right_frame = Frame(master=list_item_frame)
    
    # Labels for attributes
    name_lbl = Label(right_frame, text="Name: " + character.name, font=("Calibri", 12), padx=7.5).pack(anchor=W, expand=True)
    species_lbl = Label(right_frame, text="Species: " + character.species, font=("Calibri", 12), padx=7.5).pack(anchor=W, expand=True)
    gender_lbl = Label(right_frame, text="Gender: " + character.gender, font=("Calibri", 12), padx=7.5).pack(anchor=W, expand=True)
    origin_lbl = Label(right_frame, text="Origin: " + character.origin, font=("Calibri", 12), padx=7.5).pack(anchor=W, expand=True)
    status_lbl = Label(right_frame, text="Status: " + character.status, font=("Calibri", 12), padx=7.5).pack(anchor=W, expand=True)
    number_of_episodes_lbl = Label(right_frame, text="Number of episodes: " + str(character.number_of_episodes) + " Episodes", font=("Calibri", 12), padx=7.5).pack(anchor=W, expand=True)
    
    # Final placement of the frames
    right_frame.grid(row=0, column=1, sticky='we')
    list_item_frame.pack(fill=X, padx=7.5)
    list_row += 1 

# FINAL TKINTER EXECUTION
scrollable.pack(fill=BOTH, expand=True)
root.mainloop()