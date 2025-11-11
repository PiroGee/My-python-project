from string import punctuation
s = input('Enter a string: ')
for c in punctuation:
    s = s.replace(c, '')
s = s.lower()
L = s.split()
word = input('Enter a word: ')
print(word, 'appears', L.count(word), 'times.')
