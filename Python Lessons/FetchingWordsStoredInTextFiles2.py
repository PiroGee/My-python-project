# Program to search for a word in a file, count its occurrences, and replace it in user input

filename = "example.txt"  # Change to your file name

try:
    with open(filename, "r", encoding="utf-8") as file:
        file_content = file.read()

    print("File content stored in variable:")
    print(file_content)

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    file_content = ""
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    file_content = ""

def replace_word_with_dashes(text, word_to_remove):
    replacement = '-' * len(word_to_remove)
    words = text.split()
    replaced_words = [replacement if w == word_to_remove else w for w in words]
    return ' '.join(replaced_words)

def main():
    if not file_content:
        print("No file content to search. Exiting.")
        return

    word_to_search = input("Enter the word to search in the file: ")

    # Count occurrences of the word (case-sensitive, exact match)
    word_list = file_content.split()
    count = word_list.count(word_to_search)

    if count > 0:
        print()
        print(f"The word '{word_to_search}' was found {count} time(s) in the file.")
    else:
        print(f"Error: The word '{word_to_search}' was not found in the file.")
        return

    print("Enter your text stream (type 'exit' to quit):")
    while True:
        text = input("Text: ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break

        modified_text = replace_word_with_dashes(text, word_to_search)
        modified_text = replace_word_with_dashes(modified_text, 'fool')
        modified_text = replace_word_with_dashes(modified_text, 'idiot')

        print("Modified Text:")
        print(modified_text)
        print("-" * 10)

if __name__ == "__main__":
    main()
