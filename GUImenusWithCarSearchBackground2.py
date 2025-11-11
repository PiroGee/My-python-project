from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import os

def launch_car_navi():
    file_path = os.path.abspath("GUICarNavi4FilterByPriceBrandReset.py")
    subprocess.Popen(["python", file_path])

def open_callback():
    filename = askopenfilename()
    if filename:
        open_window = Toplevel(root)
        open_window.title("Open File")
        Label(open_window, text=f"Selected file: {filename}").pack(padx=20, pady=20)

def saveas_callback():
    filename = asksaveasfilename()
    if filename:
        save_window = Toplevel(root)
        save_window.title("Save As")
        Label(save_window, text=f"File will be saved as: {filename}").pack(padx=20, pady=20)

def about_callback():
    about_window = Toplevel(root)
    about_window.title("About")
    Label(about_window, text="This page tells you about the company. When it was incorporated, where its head office is located and the work culture.").pack(padx=20, pady=20)

# Main window
root = Tk()
root.title("Car Search App")
root.geometry("400x300")

# Menu bar
menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Open', command=open_callback)
file_menu.add_command(label='Save as', command=saveas_callback)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='About', command=about_callback)
menu.add_cascade(label="Help", menu=help_menu)

# Main content area
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

Label(main_frame, text="Welcome to Neutron Car App", font=("Arial", 14)).pack(pady=40)
Button(main_frame, text="Launch Full Car Navigator", command=launch_car_navi).pack(pady=10)

root.mainloop()
