# Задание 2.
#
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

from sys import exit


class OwnClass(Exception):
    def __init__(self, text):
        self.text = text


number1 = float(input("Введите первое число: "))
number2 = float(input("Введите первое число: "))

try:
    if number2 == 0:
        raise OwnClass("Деление на ноль невозможно")
    result = number1 / number2
except OwnClass as error:
    print(error)
else:
    print(f"Результат деления первого числа на второе: {result}")