"""
Задание 5.

Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""

import subprocess
import chardet

args = ['ping', 'yandex.ru']
yandex_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in yandex_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))

args = ['ping', 'youtube.com']
youtube_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in youtube_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('utf-8')
    print(line.decode('utf-8'))
