from tkinter import *
from PIL import Image, ImageTk

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
filtered_cars = cars.copy()

def update_display():
    if not filtered_cars:
        name_label.config(text="No cars found")
        price_label.config(text="")
        image_label.config(image="", text="Image not available")
        count_label.config(text="")
        return

    car = filtered_cars[current_index]
    name_label.config(text=car["name"])
    price_label.config(text=f"₦{car['price']:,}")
    count_label.config(text=f"Cars found: {len(filtered_cars)}")

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
    if filtered_cars:
        current_index = (current_index + 1) % len(filtered_cars)
        update_display()

def prev_car():
    global current_index
    if filtered_cars:
        current_index = (current_index - 1) % len(filtered_cars)
        update_display()

def search_by_budget():
    global filtered_cars, current_index
    try:
        budget = int(budget_entry.get())
        brand = brand_entry.get().lower()
        filtered_cars = [car for car in cars if car["price"] <= budget and brand in car["name"].lower()]
        filtered_cars.sort(key=lambda x: x["price"])  # Sort by price
        current_index = 0
        update_display()
    except ValueError:
        name_label.config(text="⚠️ Enter a valid number")
        price_label.config(text="")
        image_label.config(image="", text="")
        count_label.config(text="")

root = Tk()
root.title("Neutron Cars")

Label(root, text="Enter your budget (₦):", font=('Arial', 14)).pack(pady=5)
budget_entry = Entry(root, font=('Arial', 14))
budget_entry.pack(pady=5)

Label(root, text="Filter by brand/model (optional):", font=('Arial', 14)).pack(pady=5)
brand_entry = Entry(root, font=('Arial', 14))
brand_entry.pack(pady=5)

Button(root, text="Search", font=('Arial', 12), bg="#add8e6", command=search_by_budget).pack(pady=5)

name_label = Label(root, text="", font=('Arial', 16))
name_label.pack(pady=10)

image_label = Label(root)
image_label.pack()

price_label = Label(root, text="", font=('Arial', 14), fg="green")
price_label.pack(pady=10)

count_label = Label(root, text="", font=('Arial', 12), fg="blue")
count_label.pack(pady=5)

nav_frame = Frame(root)
nav_frame.pack(pady=10)

Button(nav_frame, text="Previous", command=prev_car).pack(side=LEFT, padx=20)
Button(nav_frame, text="Next", command=next_car).pack(side=RIGHT, padx=20)

update_display()
root.mainloop()
