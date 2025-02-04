# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
ipmask = input("Введите адрес с маской: ").split("/")
ip1,ip2,ip3,ip4 = ipmask[0].split(".")
mask = int(ipmask[-1])
mask_bin = "1" * mask + "0" * (32 - mask)
m1,m2,m3,m4 = mask_bin[0:8], mask_bin[8:16], mask_bin[16:24], mask_bin[24:32]

template = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4}
{9:<10}{10:<10}{11:<10}{12:<10}
{5}  {6}  {7}  {8}
'''
print(template.format(int(ip1), int(ip2), int(ip3), int(ip4), mask,
                      m1, m2, m3, m4,
                      int(m1, 2), int(m2, 2), int(m3, 2), int(m4, 2)))
