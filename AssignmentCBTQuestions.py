# List of available cars with their prices
ques = {
    "Convert 2km to meters":2000,
    "what is the boiling temperature of water in celcius":100,
    "Convert 10meters to centimeters" :1000,
    "Square root of 25?":5,
    "How many sides does a rectangle have?":4,
    "Capital of Nigeria?":"Abuja",
    "Capital of Imo state?":"Owerri",
    "What month does Nigeria celebrates its independence in a year":"october",
    "How many letters does the Alphabet has?":26,
    "How many days in 3 weeks":21
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
count = 0
for key in ques:
    #count = 0
    
    print("question 1 : Convert 2km to meters")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["Convert 2km to meters"]:
        count=count+1
    
    print("Question 2: what is the boiling temperature of water in celcius")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["what is the boiling temperature of water in celcius"]:
        count=count+1
        

    print("question 3 : Convert 10meters to centimeters")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["Convert 10meters to centimeters"]:
        count=count+1

    print("question 4 : Square root of 25?")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["Square root of 25?"]:
        count=count+1

    print("question 5 : How many sides does a rectangle have?")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["How many sides does a rectangle have?"]:
        count=count+1

    print("question 6 : Capital of Nigeria?")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["Capital of Nigeria?"]:
        count=count+1
    
    print("question 7 : Capital of Imo state?")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["Capital of Imo state?"]:
        count=count+1


    print("question 8 : What month does Nigeria celebrates its independence in a year")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["What month does Nigeria celebrates its independence in a year"]:
        count=count+1

    print("question 9 : How many letters does the Alphabet has?")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["How many letters does the Alphabet has?"]:
        count=count+1

    print("question 10 : How many days in 3 weeks")
    stud_ans = input("Provide your answer: ")
    if stud_ans == ques["How many days in 3 weeks"]:
        count=count+1
        
    print('Total number of correct questions: ', count)
    break

    if stud_ans.lower() == "exit":
        print("You exited the Exam. Goodbye!")
        break
