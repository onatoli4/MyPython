# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
temp = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}'''
with open("ospf.txt") as f:
    for line in f:
        _,ip,ad,_,hop,time,intf = line.replace(",", "").replace("[", "").replace("]", "").split()
        print(temp.format(ip, ad, hop, time, intf))