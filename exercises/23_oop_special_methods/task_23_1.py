# -*- coding: utf-8 -*-

"""
Задание 23.1

В этом задании необходимо создать класс IPAddress.

При создании экземпляра класса, как аргумент передается IP-адрес и маска,
а также должна выполняться проверка корректности адреса и маски:
* Адрес считается корректно заданным, если он:
   - состоит из 4 чисел разделенных точкой
   - каждое число в диапазоне от 0 до 255
* маска считается корректной, если это число в диапазоне от 8 до 32 включительно

Если маска или адрес не прошли проверку, необходимо сгенерировать
исключение ValueError с соответствующим текстом (вывод ниже).

Также, при создании класса, должны быть созданы два атрибута экземпляра:
ip и mask, в которых содержатся адрес и маска, соответственно.

Пример создания экземпляра класса:
In [1]: ip = IPAddress('10.1.1.1/24')

Атрибуты ip и mask
In [2]: ip1 = IPAddress('10.1.1.1/24')

In [3]: ip1.ip
Out[3]: '10.1.1.1'

In [4]: ip1.mask
Out[4]: 24

Проверка корректности адреса (traceback сокращен)
In [5]: ip1 = IPAddress('10.1.1/24')
---------------------------------------------------------------------------
...
ValueError: Incorrect IPv4 address

Проверка корректности маски (traceback сокращен)
In [6]: ip1 = IPAddress('10.1.1.1/240')
---------------------------------------------------------------------------
...
ValueError: Incorrect mask

"""

class IPAddress:
    def __init__(self, ip_mask):
        self.ip, self.mask = self._checking(ip_mask)
    
    def _checking(self, ip_mask):
        ip, mask = ip_mask.split('/')
        if not 8 <= int(mask) <= 32:
            raise ValueError ("Incorrect mask")
        ip_list = ip.split('.')
        if len(ip_list) != 4:
            raise ValueError ("Incorrect IPv4 address")
        for i in ip_list:
            if not i or not 0 <= int(i) <= 255:
                raise ValueError ("Incorrect IPv4 address")
        return ip, int(mask)
    
if __name__ == "__main__":
    ip1 = IPAddress('10.1.1.1/24')
    print(ip1.ip)
    print(ip1.mask)