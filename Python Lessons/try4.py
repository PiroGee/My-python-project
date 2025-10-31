# List of available cars with their prices
cars = {
    "Toyota Corolla": 4500000,
    "Honda Civic": 5200000,
    "Ford Focus": 4800000,
    "Hyundai Elantra": 4300000,
    "Kia Rio": 4000000,
    "BMW 3 Series": 8500000,
    "Mercedes-Benz C-Class": 9000000,
    "Tesla": 300000000,
    "Volkswagen Golf": 4700000
}

for key in cars:
    print(key, '-'*10, cars[key])

"""new_def = input('Enter a new price for Tesla: ')"""

new_name = input('Enter the name for new car: ')
new_def = input('Enter a new price for new car: ')

for key in cars:
    cars['new_name'] = new_def
    print(key, '-'*10, cars[key])
