# 2. Вводятся 3 целых числа. Напишите программу, которая определяет, какое
# из них четное.

# Запрос трех чисел у пользователя
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a % 2 == 0:
    print("Число", a, "четное.")
else:
    print("Число", a, "нечетное.")

if b % 2 == 0:
    print("Число", b, "четное.")
else:
    print("Число", b, "нечетное.")

if c % 2 == 0:
    print("Число", c, "четное.")
else:
    print("Число", c, "нечетное.")
