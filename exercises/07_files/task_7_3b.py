# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = []
with open('CAM_table.txt') as f:
    for line in f:
        words = line.split()
        if words and words[0].isdigit():
            vlan, mac, _, intf = words
            result.append([int(vlan), mac, intf])
myvlan = int(input("Введите номер VLAN: "))
vlan_ex = False
for vlan, mac, intf in sorted(result):
    if vlan == myvlan:
        print(f"{vlan:<9}{mac:<20}{intf}")
        vlan_ex = True
if not vlan_ex:
    print("Такого VLAN нет")