'''import sys


s = [i.strip('\n').replace(',', ' ').replace('—', ' ').replace('.', ' ').replace('-', ' ').split()
for i in sys.stdin.readlines()]
A = {}
max_ = 0
for i in s:
for j in i:
A[j.lower()] = A.get(j.lower(), 0) + 1
if A[j.lower()] > max_:
max_ = A[j.lower()]
print(A)
print(sorted(list(sorted(, reverse=True))[:10], reverse=True))
'''
import random


n = 1000000
# точность вычислений
k = 0
for _ in range(n):
    k += random.random() ** 2 + random.random() ** 2 <= 1
    # проверяем что точка в окружности или на её поверхности --> x ** 2 + y ** 2 <= 1
pi = 4 * k / n
# т.к. работаем в первой четверти из 4, то умножаем на 4
print(pi)

