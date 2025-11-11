from tkinter import *
from PIL import Image, ImageTk  # Make sure Pillow is installed

cars = [
    {"name": "Toyota Corolla", "price": 4500000, "image": "toyota_corolla.jpg"},
    {"name": "Honda Civic", "price": 5200000, "image": "honda_civic.jpg"},
    {"name": "Ford Focus", "price": 4800000, "image": "ford_focus.jpg"},
    {"name": "Hyundai Elantra", "price": 4300000, "image": "hyundai_elantra.jpg"},
    {"name": "Kia Rio", "price": 4000000, "image": "kia_rio.jpg"},
    {"name": "BMW 3 Series", "price": 8500000, "image": "bmw_3_series.jpg"},
    {"name": "Mercedes-Benz C-Class", "price": 9000000, "image": "mercedes_c_class.jpg"},
    {"name": "Volkswagen Golf", "price": 4700000, "image": "volkswagen_golf.jpg"}
]

current_index = 0

def update_display():
    car = cars[current_index]
    name_label.config(text=car["name"])
    price_label.config(text=f"₦{car['price']:,}")
    try:
        img = Image.open(car["image"])
        img = img.resize((300, 200))
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo
    except Exception as e:
        image_label.config(text="Image not found", image="")
        print("Image error:", e)

def next_car():
    global current_index
    current_index = (current_index + 1) % len(cars)
    update_display()

def prev_car():
    global current_index
    current_index = (current_index - 1) % len(cars)
    update_display()

root = Tk()
root.title("Neutron Cars")

name_label = Label(root, text="", font=('Arial', 16))
name_label.pack(pady=10)

image_label = Label(root)
image_label.pack()

price_label = Label(root, text="", font=('Arial', 14), fg="green")
price_label.pack(pady=10)

nav_frame = Frame(root)
nav_frame.pack(pady=10)

Button(nav_frame, text="Previous", command=prev_car).pack(side=LEFT, padx=20)
Button(nav_frame, text="Next", command=next_car).pack(side=RIGHT, padx=20)

update_display()
root.mainloop()
