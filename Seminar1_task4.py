# Задание 4.
#
# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите
# прибыль фирмы в расчете на одного сотрудника.
#
# Пример:
# Введите выручку фирмы: 1000
# Введите издержки фирмы: 500
# Финансовый результат - прибыль. Ее величина: 500
# Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
# Рентабельность выручки = 0.5
# Введите численность сотрудников фирмы: 10
# Прибыль фирмы в расчете на одного сотрудника = 50.0

revenue = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
fin_res = revenue - costs
if fin_res > 0:
    print(f"Финансовый результат - прибыль. Ее величина: {fin_res}")
    profit = fin_res / revenue
    print(f"Рентабельность выручки = {profit}")
    employees = int(input("Введите численность сотрудников фирмы: "))
    profit_per_employee = fin_res / employees
    print(f"Прибыль фирмы в расчете на одного сотрудника= {profit_per_employee}")
else:
    print("Финансовый результат - убыток")
