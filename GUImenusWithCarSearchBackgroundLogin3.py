from tkinter import *
from PIL import Image, ImageTk  # ✅ For JPG image support
import subprocess
import os

# Global login state
is_logged_in = False

def show_car_navigator():
    try:
        file_path = os.path.abspath("GUICarNavi4FilterByPriceBrandReset.py")
        subprocess.Popen(["python", file_path])
    except Exception as e:
        error_window = Toplevel(root)
        error_window.title("Error")
        Label(error_window, text=f"Failed to load car navigator:\n{e}").pack(padx=20, pady=20)

def login_callback():
    def attempt_login():
        username = username_entry.get()
        password = password_entry.get()

        if username == "admin" and password == "password":
            global is_logged_in
            is_logged_in = True
            Label(login_window, text="Login successful!", fg="green").grid(row=3, columnspan=2, pady=10)
            login_window.after(1000, login_window.destroy)
            root.after(1200, show_car_navigator)
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

# Main window
root = Tk()
root.title("Car Search App")
root.geometry("400x400")

# Menu bar
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Login', command=login_callback)
file_menu.add_command(label='About', command=about_callback)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

# Main content
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

Label(main_frame, text="Welcome to Neutron Car App", font=("Arial", 14)).pack(pady=20)

# Load and display JPG image
try:
    img = Image.open("mustang.jpg")  # ✅ Your car image
    img = img.resize((300, 180))  # Optional: resize to fit nicely
    car_img = ImageTk.PhotoImage(img)
    car_label = Label(main_frame, image=car_img)
    car_label.image = car_img  # Keep reference
    car_label.pack(pady=10)
except Exception as e:
    Label(main_frame, text="(Car image not found)", fg="red").pack(pady=10)

root.mainloop()
