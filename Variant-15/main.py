# 1. Выразите следующие выражения на Python, напишите программы для
# вычисления их со следующими значениями: а = 14, b = 8, с = 452, г = 41
# a) S = a + b + ac;
# b) P = πr2 + ac.

a = 14
b = 8
c = 452
r = 41
pi = 3.14

S = a + b + a * c # a
P = pi * (r ** 2) + a * c   # b

print("Значение S:", S)
print("Значение P:", P)
