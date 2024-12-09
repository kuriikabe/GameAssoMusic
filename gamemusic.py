import tkinter as tk
from tkinter import *

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

# Create a label
label = Label(gui, text="Press the button to show character-game associations!", bg="white")
label.pack(pady=10)

# Create a button
button = Button(gui, text="Show Associations", command=button_click)
button.pack(pady=5)

# Create a listbox to display results
result_listbox = Listbox(gui, width=50, height=10)
result_listbox.pack(pady=10)

# Run the main event loop
gui.mainloop()
