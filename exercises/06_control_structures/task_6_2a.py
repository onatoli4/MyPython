# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ip = input("Введите IP-адрес в формате x.x.x.x: ")
ip_list = ip.split(".")
ip_valid = True

if len(ip_list) != 4:
    ip_valid = False
else:
    for octet in ip_list:
        if not octet.isdigit() or int(octet) < 0 or int(octet) > 255:
            ip_valid = False
            break
if ip_valid:
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
else:           
    print("Неправильный IP-адрес")