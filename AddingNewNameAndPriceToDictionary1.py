# The Dictionary structure
prod = {'tylenol':15000,
        'sitagliptin':9000,
        'advil':18000,
        'Actropen':8000,
        'Ceftran Forte': 5000
        }

cont = True

while cont:
    print('Welcome Admin!!')
    proceed = input('Enter "yes" or "no" to continue: ').strip().lower()
    
    
    if proceed == 'no':
        print('Thank you for your time. Goodbye!')
        break
    
    while True:
        new_name = input('Enter the name of the new product: ')
        try:
            new_price = eval(input('Enter the price of the new product: '))
        except ValueError:
            print("Invalid price. Please enter a numeric value.")
            continue


        prod[new_name] = new_price
        
        print("\nCurrent Product List:")
        for key in prod:
            print(f"{key} {'-'*20} # {prod[key]}")
            
        proceed = input('Do you wish to continue? Select "yes" or "no": ').strip().lower()
        if proceed == 'no':
            cont = False
            print('Thank you for your time. Goodbye!')
            break
