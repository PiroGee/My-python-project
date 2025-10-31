# The Dictionary structure
prod = {
    'tylenol': 15000,
    'sitagliptin': 90000,
    'advil': 18000,
    'Actropen':8000,
    'Ceftran Forte': 5000
}

cont = True

while cont:
    print('Welcome Admin!!')
    proceed = input('Enter yes or no to continue: ').strip().lower()

    if proceed == 'no':
        print('Thank you for your time. Goodbye!')
        break

    while True:
        new_name = input('Enter the name of the new product: ')
        try:
            new_price = float(input('Enter the price of the new product (in Naira): '))
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue

        prod[new_name] = new_price

        for key in prod:
            print(f"{key} {'-'*20} ₦{prod[key]:,.2f}")

        

        try:
            max_price = float(input("\nEnter a Naira amount to filter products below that price: "))
            print(f"\nProducts priced below ₦{max_price:,.2f}:")
            found = False
            for key, value in prod.items():
                if value < max_price:
                    print(f"{key} - ₦{value:,.2f}")
                    found = True

                    
            if not found:
                print("No products found below that price.")
        except ValueError:
            print("Invalid input. Skipping price filter.")

            
        print("\nBelow is the Current Product List:")
        for key in prod:
            print(f"{key} {'-'*20} ₦{prod[key]:,.2f}")

        proceed = input('\nDo you wish to continue? Select yes or no: ').strip().lower()
        if proceed == 'no':
            cont = False
            print('Thank you for your time. Goodbye!')
            break
