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
cars['Tesla Model Z'] = 300000000
print(cars)
nnew = ('Enter the name of the new car: ')
pnew = ('Enter the price')
cars.insert(0,nnew)
cars.insert(0,pnew)
for key in cars:
    print(key)

"""for i in cars:
    print(i)"""
#print(list(cars))
# Ask the buyer for their budget
try:
    max_price = int(input("Enter the maximum price you can afford for a car (in Naira): "))

    # Filter and display cars within budget
    affordable_cars = {model: price for model, price in cars.items() if price <= max_price}

    if affordable_cars:
        print("\nCars within your budget:")
        for model, price in affordable_cars.items():
            print(f"- {model}: ₦{price:,}")
    else:
        print("\nSorry, there are no cars available within your budget.")
except ValueError:
    print("Please enter a valid number.")
