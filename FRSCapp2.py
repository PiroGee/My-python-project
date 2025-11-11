import random

# List of available questions with their answers
ques = {
    "What does FRSC stand for?": "Federal Road Safety Corps",
    "What is the maximum legal Blood Alcohol Concentration (BAC) limit for drivers in Nigeria?": "0.05%",
    "What does a RED light mean?": "stop",
    "Which agency is responsible for vehicle registration in Nigeria?": "Federal Road Safety Corps",
    "Which of the following is a synonym for ‘cautious’?": "careful",
    "What is the meaning of a double yellow line on the road?": "no overtaking",
    "What is the full meaning of VIO?": "Vehicle Inspection Officer",
    "What is the emergency number for FRSC in Nigeria?": "122",
    "What does a green traffic light mean?": "go",
    "What is the speed limit in urban areas for cars in Nigeria(in km/hr)?": "50"
}

# Predefined users with ID and password
users = {
    "admin01": "admin123",
    "stud01": "stud123",
    "stud02": "stud1234"
}

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
                print("\nUpdated Questions:")
                for key in ques:
                    print(key, '_' * 10, ques[key])

            elif choice == "2":
                new_userID = input("Enter the new student's User ID: ").strip()
                new_pin = input("Enter the PIN: ").strip()
                users[new_userID] = new_pin
                print(f"✅ '{new_userID}' was added successfully with PIN '{new_pin}'.\n")

    else:
        print("Welcome to your FRSC Exams!")
        print("Type 'submit' anytime to quit.\n")

        count = 0
        print("Starting your exam...\n")

        # Shuffle questions
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
        # Calculate and display grade
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

























