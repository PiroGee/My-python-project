num = int(input('Enter a number for temperature conversion '))
Temp = input('What is the unit of temperature entered (c or f): ')

if Temp == 'c':
    print('The temperature in Fahrenheit is ', 9/5*(num+32))
elif Temp == 'f':
    print('The temperature in Celscius is ', (5/9)*num-32)
else:
    print('Invalid')
