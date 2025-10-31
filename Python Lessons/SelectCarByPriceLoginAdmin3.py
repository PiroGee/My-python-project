
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
    "admin01": "admin123",
    "staff01": "staff123"
}
logout = False
run_status = 'yes'
print("Welcome to Neutron Cars!")


while logout == False:
    run_status = input("Continue? (type 'yes or no'): ")
    print("Please log in to continue.\n")
    if run_status == 'yes':
        logout = False
    else:
        logout = True
        print('Thank you for using Neutron Cars! Goodbye')
        break
        exit()
    
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

    # Admin menu
    if user_id == "admin01":
        while True:
            print("Admin Options:")
            print("1. Add new car to inventory")
            print("2. Search for cars by budget")
            print("Type 'exit' to quit.\n")

            choice = input("Enter your choice (1 or 2): ")

            if choice == "exit":
                print("Thank you for using Neutron Cars. Goodbye!")
                break

            elif choice == "1":
                car_name = input("Enter the name of the new car: ")
                car_price_input = input("Enter the price of the car (in Naira): ")

                try:
                    car_price = int(car_price_input)
                    cars[car_name] = car_price
                    print(f"✅ '{car_name}' added successfully at ₦{car_price:,}.\n")
                except ValueError:
                    print("❌ Invalid price. Please enter a number.\n")

            elif choice == "2":
                user_input = input("Enter the maximum price you can afford (in Naira): ")

                try:
                    max_price = int(user_input)
                    affordable_cars = {model: price for model, price in cars.items() if price <= max_price}

                    if affordable_cars:
                        print("\nCars within your budget:")
                        for model, price in affordable_cars.items():
                            print(f"- {model}: ₦{price:,}")
                    else:
                        print("\nSorry, no cars available within your budget.")
                    print()
                except ValueError:
                    print("❌ Please enter a valid number.\n")

            else:
                print("Invalid option. Please choose 1, 2, or 'exit'.\n")

    # Regular user menu
    else:
        print("Type 'exit' anytime to quit.\n")
        while True:
            user_input = input("Enter the maximum price you can afford for a car (in Naira): ")

            if user_input.lower() == "exit":
                print("Thank you for using Neutron Cars. Goodbye!")
                break

            try:
                max_price = int(user_input)
                affordable_cars = {model: price for model, price in cars.items() if price <= max_price}

                if affordable_cars:
                    print("\nCars within your budget:")
                    for model, price in affordable_cars.items():
                        print(f"- {model}: ₦{price:,}")
                else:
                    print("\nSorry, no cars available within your budget.")
                print()
            except ValueError:
                print("❌ Please enter a valid number.\n")


