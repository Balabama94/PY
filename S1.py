# n = int(input())
# m = int(input())

n = 700
m = 21000
if m % n == 0:
    result = m // n 
else: 
    result = m // n + 1
print(f'что бы проехать на машине {m} км, нужно ехать {result} дн')