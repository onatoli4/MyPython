# -*- coding: utf-8 -*-

"""
Задание 24.2b

Скопировать класс MyNetmiko из задания 24.2a.

Дополнить функционал метода send_config_set netmiko и добавить в него проверку
на ошибки с помощью метода _check_error_in_command.

Метод send_config_set должен отправлять команды по одной и проверять каждую на ошибки.
Если при выполнении команд не обнаружены ошибки, метод send_config_set возвращает
вывод команд.

In [2]: from task_24_2b import MyNetmiko

In [3]: r1 = MyNetmiko(**device_params)

In [4]: r1.send_config_set('lo')
---------------------------------------------------------------------------
ErrorInCommand                            Traceback (most recent call last)
<ipython-input-2-8e491f78b235> in <module>()
----> 1 r1.send_config_set('lo')

...
ErrorInCommand: При выполнении команды "lo" на устройстве 192.168.100.1 возникла ошибка "Incomplete command."

"""
class ErrorInCommand(Exception):
    """
    Исключение генерируется, если при выполнении команды на оборудовании,
    возникла ошибка.
    """

from netmiko.cisco.cisco_ios import CiscoIosSSH
import re

device_params = {
    "device_type": "cisco_ios",
    "ip": "192.168.100.1",
    "username": "cisco",
    "password": "cisco",
    "secret": "cisco",
}

class MyNetmiko(CiscoIosSSH):
    def __init__(self, **device_params):
        super().__init__(**device_params)
        self.enable()

    def _check_error_in_command(self, command, output):
        match = re.search(r'% (.*)', output)
        if match:
            raise ErrorInCommand(f'При выполнении команды "{command}" '
                                 f'на устройстве {self.host} '
                                 f'возникла ошибка {match.group(1)}')

    def send_command(self, command):
        output = super().send_command(command)
        self._check_error_in_command(command, output)
        return output

    def send_config_set(self, commands):
        result = ''
        if type(commands) == str:
            commands = [commands]
        for command in commands:
            output = super().send_config_set(command, exit_config_mode=False)
            self._check_error_in_command(command, output)
            result += output
        return result

if __name__ == "__main__":
    r1 = MyNetmiko(**device_params)
    print(r1.send_config_set(['logging 10.10.10.1', 'a']))