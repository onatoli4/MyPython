# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
from tabulate import tabulate

def print_ip_table(ip_list):
    ip_dict = {'Reachable': ip_list[0], 'Unreachable': ip_list[1]}
    print(tabulate(ip_dict, headers="keys"))

if __name__ == '__main__':
    print_ip_table((['1.1.1.1', '2.2.2.2'], ['3.3.3.3', '4.4.4.4']))
