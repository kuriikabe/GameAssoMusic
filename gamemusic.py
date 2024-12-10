import tkinter as tk
from tkinter import *
from playsound import playsound
import os

# Initialize GUI
gui = Tk()
gui.configure(background="white")
gui.geometry("400x300")
gui.title("Character and Game Associations")

# Function to process and display associations
def button_click():
    # Clear previous content
    result_listbox.delete(0, END)
    
    # Create associations and display them
    name = ["Aya Brea", "Tifa", "2B", "Kaine", "Ann"]
    games = ["Parasite Eve", "Final Fantasy 7", "Nier Automata", "Nier Replicant", "Persona 5"]
    
    for names, game in zip(name, games):
        result_listbox.insert(END, f"{names} is from {game}")
        print(f"{names} is from {game}")  # Debugging line for console

# Function to play sound
def play_sound():
    # Ensure the file path is properly formatted
    sound_path = r'C:\Users\msree\Downloads\arise.wav'  # Raw string to handle backslashes
    
    try:
        if not os.path.exists(sound_path):
            raise FileNotFoundError(f"File not found: {sound_path}")
        playsound(sound_path)
    except FileNotFoundError as fnf_error:
        print(f"File not found error: {fnf_error}")
    except Exception as e:
        print(f"Error: {e}")
        
# Create a label
label = Label(gui, text="Press the button to show character-game associations!", bg="white")
label.pack(pady=10)

# Create a button for associations
button = Button(gui, text="Show Associations", command=button_click)
button.pack(pady=5)

# Create a button for playing the sound
sound_button = Button(gui, text="Play Aya Brea Theme", command=play_sound)
sound_button.pack(pady=5)

# Create a listbox to display results
result_listbox = Listbox(gui, width=50, height=10)
result_listbox.pack(pady=10)

# Run the main event loop
gui.mainloop()
