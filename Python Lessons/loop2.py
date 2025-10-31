from random import randint
num = eval(input('Enter a number: '))
x = randint(1,10)
if num == x:
    print('Correct, the number is', x)
else:
    print('wrong! correct is', x)
