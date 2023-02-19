# Задание 1.
#
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
# который должен принимать данные (список списков) для формирования матрицы.
#
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
#
# Далее реализовать перегрузку метода add() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
#
# Пример:
# 1 2 3
# 4 5 6
# 7 8 9
#
# 1 2 3
# 4 5 6
# 7 8 9
#
# Сумма матриц:
# 2 4 6
# 8 10 12
# 14 16 18

import copy


class Matrix:

    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, second):
        if len(self.matrix) != len(second.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + second.matrix[i][k]
        return Matrix(res)

    def __str__(self):
        st = ''
        for i in range(len(self.matrix)):
            st = st + '\t'.join(map(str, self.matrix[i])) + '\n'
        return st


matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mtrx1 = Matrix(matrix1)
mtrx2 = Matrix(matrix2)
result = mtrx1 + mtrx2

print(f'Первая матрица: \n{mtrx1}')
print(f'Вторая матрица: \n{mtrx2}')
print(f'Сумма матриц: \n{result}')
