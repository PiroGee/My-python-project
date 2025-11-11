def generate_times_table(number, up_to=12):
    print(f"\nMultiplication Table for {number}:\n")
    for i in range(1, up_to + 1):
        result = number * i
        print(f"{number} x {i} = {result}")

# Example usage
num = int(input("Enter a number to generate its times table: "))
generate_times_table(num)
