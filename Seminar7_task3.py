# Задание 3.
# Реализовать базовый класс Worker (работник),
# в котором определить публичные атрибуты name, surname, position (должность),
# и защищенный атрибут income (доход). Последний атрибут должен ссылаться
# на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
# получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        print(f'{self.name} {self.surname} Должность - {self.position}')

    def get_total_income(self):
        print(f'Доход с учетом премии: '
              f'{self._income["wage"] + self._income["bonus"]}')


employee1 = Position('Максим', 'Петров', 'CEO', 200000, 100000)
employee2 = Position('Арсений', 'Иванов', 'Department head', 150000, 50000)
employee3 = Position('Богдан', 'Титов', 'Specialist', 50000, 10000)

employee1.get_full_name()
employee1.get_total_income()
employee2.get_full_name()
employee2.get_total_income()
employee3.get_full_name()
employee3.get_total_income()
