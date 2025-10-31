file_path = 'example.txt'

target = input("Word to replace: ")
replacement = input("New word: ")

with open(file_path, 'r') as f:
    lines = f.readlines()

new_lines = []
for i, line in enumerate(lines):
    if target in line:
        print(f"Found on line {i+1}")
    new_lines.append(line.replace(target, replacement))

with open(file_path, 'w') as f:
    f.writelines(new_lines)

print("\nUpdated content:\n")
for line in new_lines:
    print(line, end='')
