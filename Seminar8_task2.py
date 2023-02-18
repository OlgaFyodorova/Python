# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


with open("Seminar8_task2.txt", "r", encoding='utf-8') as my_file:
    text = my_file.readlines()
    i = 0
    for el in text:
        i += 1
        print(f"В {i}-й строке {len(el.split())} слов")
    print(f"Количество строк в файле - {len(text)}")
