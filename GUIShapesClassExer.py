from tkinter import *
root = Tk()
root.title('Great Shapes')
#root.geometry('300x300')
canvas = Canvas(width=200, height=200, bg='white')

canvas.create_oval(20,50,90,100, fill='red')

canvas.create_rectangle(10,100,100,150, fill='blue')
canvas.pack()

mainloop()
