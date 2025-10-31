from tkinter import*
def calculate():
    p = int(principal.get())
    r = int(rate.get())
    t = int(time.get())
    interest = (p *r *t)/100
    output_label.configure(text = 'The Interest: {:.1f}'.format(interest/100))
    principal.delete(0,END)
    rate.delete(0,END)
    time.delete(0,END)
 
root = Tk()
message_label_ = Label(text='Simple Interest Calculation', font=('Verdana', 16))
message_labelp = Label(text='Enter Principal', font=('Verdana', 16))
message_labelr = Label(text='Enter rate(%)', font=('Verdana', 16))
message_labelt = Label(text='Time(in years)',
font=('Verdana', 16))
output_label = Label(font=('Verdana', 16))
principal = Entry(font=('Verdana', 16), width=10)
rate = Entry(font=('Verdana', 16), width=4)
time = Entry(font=('Verdana', 16), width=4)
calc_button = Button(text='Ok', font=('Verdana', 16),
command=calculate)

message_label_.grid(row=0, column=0, columnspan=2)                       
message_labelp.grid(row=1, column=0)
message_labelr.grid(row=2, column=0)
message_labelt.grid(row=3, column=0)                       
                       
principal.grid(row=1, column=1)
rate.grid(row=2, column=1)
time.grid(row=3, column=1)
calc_button.grid(row=4, column=1)
output_label.grid(row=5, column=0, columnspan=2)
mainloop()
