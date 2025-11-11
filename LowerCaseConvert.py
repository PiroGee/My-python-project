s = input('Enter a string: ')
for c in ',.;:-?!()\'"':
    so = s.replace('c', 'z')
    s = s.lower()
print('',s,so)
