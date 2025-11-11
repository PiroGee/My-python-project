import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Toggle Image with One Button")

# Load the JPEG image using Pillow
image_path = "ford_focus.jpg"  # Replace with your actual image path
pil_image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(pil_image)

# Create a label to hold the image (initially hidden)
image_label = tk.Label(root, image=tk_image)
image_visible = False  # Track image visibility

# Function to toggle image visibility
def toggle_image():
    global image_visible
    if image_visible:
        image_label.pack_forget()
        toggle_button.config(text="Show Image")
        image_visible = False
    else:
        image_label.pack()
        toggle_button.config(text="Hide Image")
        image_visible = True

# Create a single toggle button
toggle_button = tk.Button(root, text="Show Image", command=toggle_image)
toggle_button.pack(pady=10)

# Run the application
root.mainloop()
