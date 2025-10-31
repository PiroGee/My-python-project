score = [56,76,85,99,48]
name = ['John', 'David', 'Smith', 'Tom', 'Jerry']

add_name = input('Enter a new name: ')
add_score = eval(input('Enter a new score: '))


name.insert(0,add_name)
score.insert(0,add_score)

lt = len(name)

print('Student Result Sheet')
for i in range(lt):
    print(name[i] + '-'*10 + str(score[i]))
print('Total number of record is: ', lt)
