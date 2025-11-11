# Program to store contents from a file into a variable

# specify the file name
filename = "example.txt"  # change to your file name

try:
    # open the file in read mode
    with open(filename, "r", encoding="utf-8") as file:
        # read the entire content of the file into a variable
        file_content = file.read()

    # print the content stored in the variable
    print("File content stored in variable:")
    print(file_content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
