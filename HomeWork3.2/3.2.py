# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. 
# Введенное число не обязательно содержится в списке.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9

# a=[10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# x=int(input())
# number=0
# for i in range(len(a)):
#     if (x-a[i])<x-number and x-a[i]>0:
#         number=a[i]
#     else:
#         i+=1
# print(a[number])

a = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input())
result = a[0]
for i in a:
     if abs(i - x) < abs(result - x):
          result = i
print(result)