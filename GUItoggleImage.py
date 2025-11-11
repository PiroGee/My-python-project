import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("JPEG Image Toggle")

# Load the JPEG image using Pillow
image_path = "ford_focus.jpg"  # Replace with your actual image path
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)

# Create a label to hold the image (initially hidden)
image_label = tk.Label(root, image=tk_image)
image_label.pack_forget()  # Hide initially

# Function to show the image
def show_image():
    image_label.pack()

# Function to hide the image
def hide_image():
    image_label.pack_forget()

# Create buttons to toggle the image
show_button = tk.Button(root, text="Show Image", command=show_image)
show_button.pack(pady=10)

hide_button = tk.Button(root, text="Hide Image", command=hide_image)
hide_button.pack(pady=10)

# Run the application
root.mainloop()
