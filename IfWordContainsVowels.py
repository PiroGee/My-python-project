# Ask the user to enter a word
word = input("Enter a word: ")

# Define the set of vowels
vowels = set("aeiouAEIOU")

# Check if any character in the word is a vowel
contains_vowel = any(char in vowels for char in word)

# Print the result
if contains_vowel:
    print("The word contains at least one vowel.")
else:
    print("The word does not contain any vowels.")
