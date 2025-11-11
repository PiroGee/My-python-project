import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import threading
import os

# Play sound in a separate thread to avoid freezing the GUI
sound_path = "He_lives_in_me_drill.mp3"  # Replace with your actual MP3 file

def play_sound():
    if os.path.exists(sound_path):
        threading.Thread(target=playsound, args=(sound_path,), daemon=True).start()

# Create main window
root = tk.Tk()
root.title("Multi-Image Toggle with MP3 Sound")

# List of image paths
image_files = ["ford_focus.jpg", "BMW_3_Series.jpg", "fordmustang.jpg"]  # Replace with your actual files
images = []
labels = []

# Load images and create labels (initially hidden)
for img_file in image_files:
    pil_img = Image.open(img_file)
    tk_img = ImageTk.PhotoImage(pil_img)
    images.append(tk_img)
    lbl = tk.Label(root, image=tk_img)
    lbl.pack_forget()
    labels.append(lbl)

# Track current image index and visibility
current_index = 0
image_visible = False

# Function to toggle image visibility
def toggle_image():
    global image_visible
    play_sound()
    if image_visible:
        labels[current_index].pack_forget()
        toggle_btn.config(text="Show Image")
        image_visible = False
    else:
        labels[current_index].pack()
        toggle_btn.config(text="Hide Image")
        image_visible = True

# Function to switch image
def switch_image(index):
    global current_index, image_visible
    if image_visible:
        labels[current_index].pack_forget()
    current_index = index
    if image_visible:
        labels[current_index].pack()

# Dropdown menu to select image
image_selector = tk.Frame(root)
image_selector.pack(pady=10)

for i, img_name in enumerate(image_files):
    btn = tk.Button(image_selector, text=f"Image {i+1}", command=lambda i=i: switch_image(i))
    btn.pack(side=tk.LEFT, padx=5)

# Toggle button
toggle_btn = tk.Button(root, text="Show Image", command=toggle_image)
toggle_btn.pack(pady=10)

# Run the app
root.mainloop()
