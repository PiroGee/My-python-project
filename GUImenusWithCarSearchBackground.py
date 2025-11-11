from tkinter import *
from tkinter.filedialog import *

def show_car_search():
    for widget in main_frame.winfo_children():
        widget.destroy()

    Label(main_frame, text="Search for Cars", font=("Arial", 14)).pack(pady=10)

    Label(main_frame, text="Car Brand:").pack()
    brand_entry = Entry(main_frame)
    brand_entry.pack(pady=5)

    Label(main_frame, text="Price Range:").pack()
    price_entry = Entry(main_frame)
    price_entry.pack(pady=5)

    def search():
        brand = brand_entry.get()
        price = price_entry.get()
        Label(main_frame, text=f"Searching for {brand} cars under {price}...", fg="blue").pack(pady=10)

    Button(main_frame, text="Search", command=search).pack(pady=10)
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

# Main content area
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=True)

# Load car search by default
show_car_search()

root.mainloop()
