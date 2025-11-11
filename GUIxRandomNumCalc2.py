from tkinter import *
import random

# Initialize score and question count
score = 0
question_count = 0

def generate_question():
    global current_num1, current_num2
    current_num1 = random.randint(1, 10)
    current_num2 = random.randint(1, 10)
    num1_label.config(text=str(current_num1))
    num2_label.config(text=str(current_num2))
    answer.delete(0, END)
    output_label.config(text="")

def calculate():
    global score, question_count

    if question_count >= 10:
        output_label.config(text=f"✅ Quiz finished! Your score: {score}/10")
        calc_button.config(state=DISABLED)
        return

    try:
        user_input = int(answer.get())
        correct_answer = current_num1 * current_num2
        if user_input == correct_answer:
            score += 1
            output_label.config(text="✅ Correct!")
        else:
            output_label.config(text=f"❌ Wrong! It was {correct_answer}")
    except ValueError:
        output_label.config(text="Please enter a valid number.")
        return  # Don't count invalid input as a question

    question_count += 1

    if question_count < 10:
        generate_question()
    else:
        output_label.config(text=f"✅ Quiz finished! Your score: {score}/10")
        calc_button.config(state=DISABLED)

root = Tk()
root.title("Kids Math Program")

Label(text='Multiply the 2 numbers below', font=('Verdana', 16)).grid(row=0, column=0, columnspan=2)

Label(text='First number:', font=('Verdana', 16)).grid(row=1, column=0)
num1_label = Label(text='?', font=('Verdana', 16))
num1_label.grid(row=1, column=1)

Label(text='Second number:', font=('Verdana', 16)).grid(row=2, column=0)
num2_label = Label(text='?', font=('Verdana', 16))
num2_label.grid(row=2, column=1)

Label(text='Your answer:', font=('Verdana', 16)).grid(row=3, column=0)
answer = Entry(font=('Verdana', 16), width=10)
answer.grid(row=3, column=1)

calc_button = Button(text='Submit', font=('Verdana', 16), command=calculate)
calc_button.grid(row=4, column=0, columnspan=2)

output_label = Label(font=('Verdana', 16))
output_label.grid(row=5, column=0, columnspan=2)

generate_question()
root.mainloop()
