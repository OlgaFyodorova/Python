# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

number1 = int(input("Введите целое положительное число: "))
number2 = number1 + number1
number3 = number1 + number1 + number1
result = str(number1) + str(number2) + str(number3)
print(result)