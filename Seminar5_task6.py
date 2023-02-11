# Задание 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой
# неудачной попытки должно сообщаться больше или меньше введенное пользователем
# число, чем то, что загадано. Если за 10 попыток число не отгадано,
# то вывести загаданное число.
# Решите через рекурсию. В задании нельзя применять циклы.

from random import randint


def random_num(user_number, random_number=randint(0, 100), count_attempt=0):
    if user_number == random_number:
        print(f'Вы угадали. Загаданное число - {random_number}')
        return

    if count_attempt == 10:
        print(f'Вы исчерпали 10 попыток. Загаданное число - {random_number}')
        return
    else:
        if user_number > random_number:
            print(f'Число больше загаданного')
        else:
            print(f'Число меньше загаданного')
    return (random_num(user_number=int(input('Попробуйте еще раз - ')),
                          count_attempt=count_attempt + 1))


print('Отгадайте число, загаданное компьютером. У Вас есть 10 '
      'попыток.')
random_num(user_number=int(input('Введите число от 0 до 100: ')))
