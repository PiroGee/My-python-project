# List of available cars with their prices
cars = {
    "Toyota Corolla": 4500000,
    "Honda Civic": 5200000,
    "Ford Focus": 4800000,
    "Hyundai Elantra": 4300000,
    "Kia Rio": 4000000,
    "BMW 3 Series": 8500000,
    "Mercedes-Benz C-Class": 9000000,
    "Volkswagen Golf": 4700000
}

# Predefined users with ID and password
users = {
    "admin": "admin123",
    "user1": "userpass"
}

print("Welcome to Neutron Cars!")
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

# Car search loop
print("Type 'exit' anytime to quit.\n")

while True:
    user_input = input("Enter the maximum price you can afford for a car (in Naira): ")

    if user_input.lower() == "exit":
        print("Thank you for using Neutron Cars. Goodbye!")
        break

    try:
        max_price = int(user_input)

        # Filter and display cars within budget
        affordable_cars = {model: price for model, price in cars.items() if price <= max_price}

        if affordable_cars:
            print("\nCars within your budget:")
            for model, price in affordable_cars.items():
                print(f"- {model}: ₦{price:,}")
        else:
            print("\nSorry, there are no cars available within your budget.")

        print("\nYou can search again or type 'exit' to quit.\n")

    except ValueError:
        print("Please enter a valid number or type 'exit' to quit.\n")
