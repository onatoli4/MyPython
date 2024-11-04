# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
    ip = input("Введите IP-адрес в формате x.x.x.x: ")
    ip_list = ip.split(".")
    ip_valid = len(ip_list) == 4
    for octet in ip_list:
        ip_valid = octet.isdigit() and 0 <= int(octet) <= 255 and ip_valid 
    if ip_valid:
        break
    print("Неправильный IP-адрес")

ip1 = int(ip_list[0])
if ip == "0.0.0.0":
    print("unassigned")
elif ip == "255.255.255.255":
    print("local broadcast")
elif ip1 > 0 and ip1 < 224:
    print("unicast")
elif ip1 > 223 and ip1 < 240:
    print("multicast")
else:
    print("unused")