# Задание 4.
# Реализуйте базовый класс Car. У данного класса должны быть следующие публичные атрибуты:
# speed, color, name, is_police (булево).
# А также публичные методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс публичный метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} повернула направо'

    def turn_left(self):
        return f'{self.name} повернула налево'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} - '
              f' {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} в норме'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} - '
              f' {self.speed}')
        if self.speed > 40:
            return f'Скорость {self.name} превышена'
        else:
            return f'Скорость {self.name} в норме'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


kia = TownCar(60, 'Black', 'KIA', False)
ferrari = SportCar(180, 'Red', 'Ferrari', False)
skoda = WorkCar(50, 'Grey', 'Skoda', False)
ford = PoliceCar(90, 'White',  'Ford', True)

print(f'{skoda.show_speed()}')
print(f'{kia.show_speed()}')
print(f'Когда {ferrari.go()}, {skoda.stop()}')
print(f'{ford.name} полицейская машина? {ford.is_police}')
print(f'{ferrari.name} полицейская машина?  {ferrari.is_police}')