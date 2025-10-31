def replace_word_with_dashes(text, word_to_remove):
    replacement = '-' * len(word_to_remove)
    # Replace whole words only, case-sensitive
    words = text.split()
    replaced_words = [replacement if w == word_to_remove else w for w in words]
    return ' '.join(replaced_words)

def main():
    print("Enter your text stream (type 'exit' to quit):")
    while True:
        text = input("Text: ")
        if text.lower() == 'exit':
            print("Goodbye!")
            break
        #word = file_content
        word = input("Enter the word to remove: ")
        modified_text = replace_word_with_dashes(text, word)
        modified_text = replace_word_with_dashes(modified_text, 'fool')
        modified_text = replace_word_with_dashes(modified_text, 'idiot')
        print("Modified Text:")
        print(modified_text)
        print("-" * 10)

if __name__ == "__main__":
    main()
