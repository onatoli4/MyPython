# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
src = argv[1]
dst = argv[2]
ignore = ["duplex", "alias", "configuration"]
with open(src) as s, open(dst, "w") as d:
    for line in s:
        words = line.split()
        words_int = set(words) & set(ignore)
        if not line.startswith("!") and not words_int:
            d.write(line)