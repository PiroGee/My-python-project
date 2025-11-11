"""
file1 = open('example.txt', 'r')
wordlist = file1.readlines()
file1.close()

# Ask user for the word to search
word_search = input("Enter the word to search in the file: ")

# Search for the word
found = False
for line in wordlist:
    if word_search.lower() in line.lower():  # Case-insensitive match
        print(f"The word '{word_search}' was found in: {line.strip()}")
        found = True

if not found:
    print("Word not found.")"""

# Read the file content
with open('example.txt', 'r') as file:
    wordlist = [line.strip() for line in file]

# Display the content
print("\n".join(wordlist))
print('-' * 30)

# Ask for the word to search
word_search = input("Enter the word to search in the file: ")

# Search and print results
#found = False
for line in wordlist:
    if word_search.lower() in line.lower():
        print(f"The word '{word_search}' was found in: {line}")
        found = True

if not found:
    print("Word not found.")


    
