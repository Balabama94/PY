# klass1 = int(input('Введите количество учеников в 1 классе '))
# klass2 = int(input())
# klass3 = int(input())
# part1 = klass1 // 2
# part2 = klass2 // 2
# part3 = klass3 // 2
# result = part1 + part2 + part3
# # print(f'количество парт для всех классов будет {result}')
# klass1 = int(input('Введите количество учеников в 1 классе '))
# part1 = klass1 // 2 if klass1 % 2 == 0 else klass1 // 2 + 1
# print(part1)

year = int(input('Введите год '))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('yes')
else:
    print('no')

print('Yes' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else 'No')

condition1 = year % 4 == 0 and year % 100 != 0
condition2 = year % 400 == 0
print('Yes' if condition1 or condition2 else 'No')