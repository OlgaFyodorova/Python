# 5. Сделайте профилирование кода любого или любых выполненных заданий
# с помощью модуля timeit, опишите результат

from timeit import timeit

print(timeit("""
x = float(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))


def my_func(x, y):
    return 1 / x ** abs(y)
    # return x ** y


print(my_func(x, y))
             
""", number=10))
