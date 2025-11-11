import random
num = int(input('Enter a number: '))
xx = random.randint(1,10)
if num == xx:
    print('print', xx)
else:
    print('failed', xx)
