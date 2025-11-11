import random
import os

# Load questions from file
def load_questions():
    questions = {}
    if os.path.exists("questions.txt"):
        with open("questions.txt", "r") as f:
            for line in f:
                if "|" in line:
                    q, a = line.strip().split("|", 1)
                    questions[q] = a
    return questions

# Save questions to file
def save_questions(questions):
    with open("questions.txt", "w") as f:
        for q, a in questions.items():
            f.write(f"{q}|{a}\n")

# Load users from file
def load_users():
    users = {}
    if os.path.exists("users.txt"):
        with open("users.txt", "r") as f:
            for line in f:
                if "|" in line:
                    uid, pwd = line.strip().split("|", 1)
                    users[uid] = pwd
    return users

# Save users to file
def save_users(users):
    with open("users.txt", "w") as f:
        for uid, pwd in users.items():
            f.write(f"{uid}|{pwd}\n")

# Initialize data
ques = load_questions()
users = load_users()

logout = False
print("Welcome to Federal Road Safety Corps!")

while not logout:
    run_status = input("Continue? (type 'yes' or 'no'): ").strip().lower()
    print("Please log in to continue.\n")
    if run_status != 'yes':
        print('Thank you for your time. Goodbye!')
        break

    # Login loop
    while True:
        user_id = input("Enter your user ID (or type 'submit' to quit): ").strip()
        if user_id.lower() == "submit":
            print("You have submitted! Goodbye")
            exit()

        password = input("Enter your password: ").strip()

        if user_id in users and users[user_id] == password:
            print(f"\nLogin successful! Welcome, {user_id}.\n")
            break
        else:
            print("Invalid ID or password. Please try again.\n")

    # Admin menu
    if user_id == "admin01":
        while True:
            print("Admin Options:")
            print("1. Add new questions")
            print("2. Register new user")
            print("Type 'exit' to quit.\n")

            choice = input("Enter your choice (1 or 2): ").strip()

            if choice.lower() == "exit":
                print("Thank you for your time!")
                break

            elif choice == "1":
                new_ques = input("Enter a new question: ").strip()
                new_ans_input = input("Enter the answer: ").strip()
                ques[new_ques] = new_ans_input
                save_questions(ques)
                print("\n✅ Question added and saved successfully!")

            elif choice == "2":
                new_userID = input("Enter the new student's User ID: ").strip()
                new_pin = input("Enter the PIN: ").strip()
                users[new_userID] = new_pin
                save_users(users)
                print(f"✅ '{new_userID}' was added successfully and saved.\n")

    else:
        print("Welcome to your FRSC Exams!")
        print("Type 'submit' anytime to quit.\n")

        count = 0
        print("Starting your exam...\n")

        questions_list = list(ques.items())
        random.shuffle(questions_list)

        for i, (question, correct_answer) in enumerate(questions_list, start=1):
            print(f"Question {i}: {question}")
            stud_ans = input("Provide your answer: ").strip()

            if stud_ans.lower() == "submit":
                print("You have submitted. Goodbye!")
                exit()

            if str(stud_ans).lower() == str(correct_answer).lower():
                count += 1

        print(f"\nExam completed. Total number of correct answers: {count} out of {len(ques)}")
        percentage = (count / len(ques)) * 100
        print(f"Your score percentage is: {percentage:.2f}%")

        if percentage < 40:
            grade = "Failed"
        elif 40 <= percentage < 50:
            grade = "Pass"
        elif 50 <= percentage < 60:
            grade = "Good"
        elif 60 <= percentage < 80:
            grade = "Very Good"
        else:
            grade = "Excellent"

        print(f"Your performance grade is: {grade}")
        break
