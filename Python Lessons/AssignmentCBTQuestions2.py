# List of questions and correct answers
ques = {
    "Convert 2km to meters": 2000,
    "what is the boiling temperature of water in celcius": 100,
    "Convert 10meters to centimeters": 1000,
    "Square root of 25?": 5,
    "How many sides does a rectangle have?": 4,
    "Capital of Nigeria?": "Abuja",
    "Capital of Imo state?": "Owerri",
    "What month does Nigeria celebrates its independence in a year": "october",
    "How many letters does the Alphabet has?": 26,
    "How many days in 3 weeks": 21
}

# Predefined users with ID and password
users = {
    "stud1": "stud123",
    "stud2": "stud1234"
}

print("Welcome to your CBT Exams!")
print("Please log in to continue.\n")

# Login loop
while True:
    user_id = input("Enter your user ID (or type 'exit' to quit): ")
    if user_id.lower() == "exit":
        print("Goodbye!")
        exit()

    password = input("Enter your password: ")

    if user_id in users and users[user_id] == password:
        print(f"\nLogin successful! Welcome, {user_id}.\n")
        break
    else:
        print("Invalid ID or password. Please try again.\n")

# Start exam
count = 0
print("Starting your exam...\n")

for i, (question, correct_answer) in enumerate(ques.items(), start=1):
    print(f"Question {i}: {question}")
    stud_ans = input("Provide your answer: ")

    # Normalize input for string answers
    if isinstance(correct_answer, str):
        if stud_ans.strip().lower() == correct_answer.lower():
            count += 1
    else:
        try:
            if int(stud_ans) == correct_answer:
                count += 1
        except ValueError:
            print("Invalid input. Expected a number.")

print(f"\nExam completed. Total number of correct answers: {count} out of {len(ques)}")
percentage = (count / len(ques)) * 100
print(f"Your score percentage is: {percentage:.2f}%")
