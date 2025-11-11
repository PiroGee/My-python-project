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



def replace_word_with_dashes(text, word_to_remove):
    replacement = '-' * len(word_to_remove)
    #Replace whole words only, case-sensitive
    words = text.split()
    replaced_words = [replacement if w == word_to_remove else w for w in words]
    return ' '.join(replaced_words)

def main():
    print("Enter your text stream (type 'exit' to quit):")
    while True:
        text = input("Text: ")
        """if text.lower() == 'exit':
            print("Goodbye!")
            break"""
        word = file_content
        modified_text = replace_word_with_dashes(text, word)
        modified_text = replace_word_with_dashes(modified_text, 'fool')
        modified_text = replace_word_with_dashes(modified_text, 'idiot')
        print("Modified Text:")
        print(modified_text)
        print("-" * 10)

if __name__ == "__main__":
    main()
