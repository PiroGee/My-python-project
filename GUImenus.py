from tkinter import *
from tkinter.filedialog import *

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

root = Tk()
root.title("Main Window")

menu = Menu(root)
root.config(menu=menu)

file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label='Open', command=open_callback)
file_menu.add_command(label='Save as', command=saveas_callback)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)
menu.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu, tearoff=0)
help_menu.add_command(label='About', command=about_callback)
menu.add_cascade(label='Help', menu=help_menu)

root.mainloop()
