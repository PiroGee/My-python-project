file = 'example.txt'

target = input("Enter word to replace: ")

# Show where the word appears
with open(file, 'r') as f:
    lines = f.readlines()

for i in range(len(lines)):
    if target in lines[i]:
        print("Found on line", i + 1)

# Ask for the new word
replacement = input("Enter new word: ")

# Replace and save
for i in range(len(lines)):
    lines[i] = lines[i].replace(target, replacement)

with open(file, 'w') as f:
    f.writelines(lines)

# Show updated content
print("\nUpdated content:\n")
for line in lines:
    print(line, end='')
