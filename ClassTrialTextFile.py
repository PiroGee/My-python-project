"""file1 = open('example.txt', 'w')
#temperatures = [line.strip() for line in open('example.txt')]
lines = [line.strip() for line in open('example.txt')]
for i in range(len(lines)):
    print(i)
print(len(lines))
file1.close()

222
# Define the path to your text file
file_path = 'example.txt'

# Read the file into a list
with open(file_path, 'r') as file:
    lines = file.readlines()

# Print each line from the list
for line in lines:
    print(line.strip())  # .strip() removes any trailing newline characters


333
file_path = 'example.txt'  # Make sure this file exists in your working directory

try:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if lines:
        print("File content:")
        for line in lines:
            print(line.strip())
    else:
        print("The file is empty.")
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")"""


file_path = 'example.txt'  # Make sure this file exists

try:
    with open(file_path, 'r') as file:
        print("File content:")
        for line in file:
            print(line.strip())  # Remove trailing newline characters
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")


