"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

words_list = ['разработка', 'администрирование', 'protocol', 'standard']

for element in words_list:
    bytes_list = str.encode(element, encoding='utf-8')
    print(bytes_list)
    print(type(bytes_list))

    string_list = bytes.decode(bytes_list, encoding='utf-8')
    print(string_list)
    print(type(string_list))
