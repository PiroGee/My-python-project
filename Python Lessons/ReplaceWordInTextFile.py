def replace_word_in_file(file_path):
    try:
        # Ask the user for the target and replacement words
        target_word = input("Enter the word you want to replace: ")
        replacement_word = input("Enter the new word: ")

        # Read the file content
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # Replace the target word with the replacement
        updated_content = content.replace(target_word, replacement_word)

        # Write the updated content back to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(updated_content)

        print(f"Replaced '{target_word}' with '{replacement_word}' successfully.")
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
replace_word_in_file('example.txt')
