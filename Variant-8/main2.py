# 2. Напишите программу, в которой вычисляется сумма цифр а и b, если
# данное целое число а делится без остатка на целое число b, не равное
# нулю, в противном случае вычисляется их произведение.

a = int(input("Введите число a: "))
b = int(input("Введите число b (не равное нулю): "))

if b != 0:
    if a % b == 0:
        otvet = a + b
    else:
        otvet = a * b
    print("Результат:", otvet)
else:
    print("Ошибка: b не должно быть равно нулю!")
