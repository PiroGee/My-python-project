"""from tkinter import *
from PIL import Image, ImageTk
import os

# Global state
is_logged_in = False
inactivity_timer = None
car_img_global = None

def reset_to_landing():
    global is_logged_in
    is_logged_in = False
    root.unbind_all("<Motion>")
    root.unbind_all("<Key>")
    for widget in root.winfo_children():
        widget.destroy()
    build_landing_page()

def restart_timer(event=None):
    global inactivity_timer
    if inactivity_timer:
        root.after_cancel(inactivity_timer)
    inactivity_timer = root.after(30000, reset_to_landing)

def build_car_filter_window():
    restart_timer()
    root.bind_all("<Motion>", restart_timer)
    root.bind_all("<Key>", restart_timer)

    for widget in root.winfo_children():
        widget.destroy()

    root.title("Car Search - Filter by Price and Name")
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)

    Label(main_frame, text="Select Car Name:", font=("Arial", 12)).pack(pady=10)
    car_names = ["Toyota", "Honda", "BMW", "Mercedes", "Ford"]
    car_name_var = StringVar(value=car_names[0])
    OptionMenu(main_frame, car_name_var, *car_names).pack()

    Label(main_frame, text="Select Price Range:", font=("Arial", 12)).pack(pady=10)
    price_ranges = ["Below $10,000", "$10,000 - $20,000", "$20,000 - $30,000", "Above $30,000"]
    price_var = StringVar(value=price_ranges[0])
    OptionMenu(main_frame, price_var, *price_ranges).pack()

    Button(main_frame, text="Search", command=lambda: print(f"Searching for {car_name_var.get()} in {price_var.get()}")).pack(pady=20)

def login_callback():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "password":
            global is_logged_in
            is_logged_in = True
            Label(login_window, text="Login successful!", fg="green").grid(row=3, columnspan=2, pady=10)
            login_window.after(1000, lambda: [login_window.destroy(), build_car_filter_window()])
        else:
            Label(login_window, text="Invalid credentials. Try again.", fg="red").grid(row=3, columnspan=2, pady=10)

    login_window = Toplevel(root)
    login_window.title("Login")

    Label(login_window, text="Username:").grid(row=0, column=0, padx=10, pady=10)
    username_entry = Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    Label(login_window, text="Password:").grid(row=1, column=0, padx=10, pady=10)
    password_entry = Entry(login_window, show="*")
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    Button(login_window, text="Login", command=attempt_login).grid(row=2, columnspan=2, pady=10)

def about_callback():
    about_window = Toplevel(root)
    about_window.title("About")
    Label(about_window, text="Neutron Cars is a car exporting company. We are keen on customers' satisfaction and comfort.").pack(padx=20, pady=20)

def build_landing_page():
    global car_img_global
    root.title("Car Search App")
    menu = Menu(root)
    root.config(menu=menu)

    file_menu = Menu(menu, tearoff=0)
    file_menu.add_command(label='Login', command=login_callback)
    file_menu.add_command(label='About', command=about_callback)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menu.add_cascade(label="File", menu=file_menu)

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=True)

    Label(main_frame, text="Welcome to Neutron Car App", font=("Arial", 14)).pack(pady=20)

    try:
        img = Image.open("mustang.jpg")
        img = img.resize((300, 180))
        car_img_global = ImageTk.PhotoImage(img)
        car_label = Label(main_frame, image=car_img_global)
        car_label.pack(pady=10)
    except Exception as e:
        Label(main_frame, text="(Car image not found)", fg="red").pack(pady=10)

# Main window
root = Tk()
root.geometry("400x400")
build_landing_page()
root.mainloop()
