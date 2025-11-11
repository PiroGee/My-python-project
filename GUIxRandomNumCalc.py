from tkinter import*
import random
def calculate():
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    correct_answer = num1*num2
    output_label.configure(text = 'The Correct Answer: {:.1f}'.format(correct_answer))
    answer.delete(0,END)
    
score = 0
for i in range(10):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    print('Question', i+1, ':', num1, ' x ', num2)
    user_input = int(answer.get())
    if user_input == correct_answer:
        score += 1
print('YOUR FINAL SCORE IS', score, 'out of 10.') 




 
root = Tk()
message_label_ = Label(text='Kids Math Program', font=('Verdana', 16))
message_labelinst = Label(text='Multiple the 2 numbers below', font=('Verdana', 16))                         
message_labelf = Label(text='First number', font=('Verdana', 16), #num1)
message_labels = Label(text='Second number', font=('Verdana', 16), #num2)

output_label = Label(font=('Verdana', 16))
answer = Entry(font=('Verdana', 16), width=16)
answer.grid(row=3, column=1)

calc_button = Button(text='Ok', font=('Verdana', 16),
command=calculate)

message_label_.grid(row=0, column=0, columnspan=2)
message_labelinst.grid(row=1, column=0, columnspan=1)
message_labelf.grid(row=2, column=0)
message_labels.grid(row=3, column=0)                       
                       
num1.grid(row=2, column=1)
num2.grid(row=3, column=1)
calc_button.grid(row=4, column=1)
output_label.grid(row=5, column=0, columnspan=2)
mainloop()
