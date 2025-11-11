from tkinter import *
import random

# Hardcoded credentials
USERNAME = "student"
PASSWORD = "math123"

# Initialize score and question count
score = 0
question_count = 0

# Main quiz window — hidden at first
root = Tk()
root.title("Kids Math Program")
root.configure(bg="#f0f8ff")  # Light blue background
root.withdraw()

def generate_question():
    global current_num1, current_num2
    current_num1 = random.randint(1, 10)
    current_num2 = random.randint(1, 10)
    num1_label.config(text=str(current_num1))
    num2_label.config(text=str(current_num2))
    answer.delete(0, END)
    feedback_label.config(text="", fg="black")
    output_label.config(text="")

def calculate():
    global score, question_count

    if question_count >= 10:
        output_label.config(text=f"✅ Quiz finished! Your score: {score}/10", fg="green")
        calc_button.config(state=DISABLED)
        return

    try:
        user_input = int(answer.get())
        correct_answer = current_num1 * current_num2
        if user_input == correct_answer:
            score += 1
            feedback_label.config(text="✅ Correct!", fg="green")
        else:
            feedback_label.config(text=f"❌ Wrong! Correct answer: {correct_answer}", fg="red")
    except ValueError:
        feedback_label.config(text="⚠️ Please enter a valid number.", fg="orange")
        return

    question_count += 1

    if question_count < 10:
        root.after(1000, generate_question)  # Wait 1 second before next question
    else:
        output_label.config(text=f"✅ Quiz finished! Your score: {score}/10", fg="blue")
        calc_button.config(state=DISABLED)

def show_quiz():
    root.deiconify()

    Label(root, text='Multiply the 2 numbers below', font=('Verdana', 18, 'bold'), bg="#f0f8ff").grid(row=0, column=0, columnspan=2, pady=10)

    Label(root, text='First number:', font=('Verdana', 14), bg="#f0f8ff").grid(row=1, column=0, sticky=E, padx=10)
    global num1_label
    num1_label = Label(root, text='?', font=('Verdana', 14), bg="#f0f8ff")
    num1_label.grid(row=1, column=1, sticky=W)

    Label(root, text='Second number:', font=('Verdana', 14), bg="#f0f8ff").grid(row=2, column=0, sticky=E, padx=10)
    global num2_label
    num2_label = Label(root, text='?', font=('Verdana', 14), bg="#f0f8ff")
    num2_label.grid(row=2, column=1, sticky=W)

    Label(root, text='Your answer:', font=('Verdana', 14), bg="#f0f8ff").grid(row=3, column=0, sticky=E, padx=10)
    global answer
    answer = Entry(root, font=('Verdana', 14), width=10)
    answer.grid(row=3, column=1, sticky=W)

    global calc_button
    calc_button = Button(root, text='Submit', font=('Verdana', 14), bg="#add8e6", command=calculate)
    calc_button.grid(row=4, column=0, columnspan=2, pady=10)

    global feedback_label
    feedback_label = Label(root, font=('Verdana', 14), bg="#f0f8ff")
    feedback_label.grid(row=5, column=0, columnspan=2)

    global output_label
    output_label = Label(root, font=('Verdana', 14), bg="#f0f8ff")
    output_label.grid(row=6, column=0, columnspan=2, pady=10)

    generate_question()

# Login window — appears first
login_window = Tk()
login_window.title("Login First")
login_window.configure(bg="#e6f2ff")

Label(login_window, text="Username:", font=('Verdana', 14), bg="#e6f2ff").grid(row=0, column=0, padx=10, pady=5)
username_entry = Entry(login_window, font=('Verdana', 14))
username_entry.grid(row=0, column=1, padx=10, pady=5)

Label(login_window, text="Password:", font=('Verdana', 14), bg="#e6f2ff").grid(row=1, column=0, padx=10, pady=5)
password_entry = Entry(login_window, font=('Verdana', 14), show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

login_msg = Label(login_window, font=('Verdana', 12), fg="red", bg="#e6f2ff")
login_msg.grid(row=3, column=0, columnspan=2)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == USERNAME and password == PASSWORD:
        login_window.destroy()
        show_quiz()
    else:
        login_msg.config(text="❌ Invalid credentials. Try again.")

Button(login_window, text="Login", font=('Verdana', 14), bg="#add8e6", command=validate_login).grid(row=2, column=0, columnspan=2, pady=10)

login_window.mainloop()
