# -*- coding: utf-8 -*-
"""
Задание 21.4

Создать функцию send_and_parse_show_command.

Параметры функции:
* device_dict - словарь с параметрами подключения к одному устройству
* command - команда, которую надо выполнить
* templates_path - путь к каталогу с шаблонами TextFSM
* index - имя индекс файла, значение по умолчанию "index"

Функция должна подключаться к одному устройству, отправлять команду show
с помощью netmiko, а затем парсить вывод команды с помощью TextFSM.

Функция должна возвращать список словарей с результатами обработки
вывода команды (как в задании 21.1a):
* ключи - имена переменных в шаблоне TextFSM
* значения - части вывода, которые соответствуют переменным

Проверить работу функции на примере вывода команды sh ip int br
и устройствах из devices.yaml.
"""
import yaml
import os
from netmiko import ConnectHandler
from task_21_3 import parse_command_dynamic

def send_and_parse_show_command(device_dict, command, templates_path):
    os.environ["NET_TEXTFSM"] = templates_path
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        output = ssh.send_command(command, use_textfsm=True)
        return output
#    attributes = {'Command': command}
#    parsing = parse_command_dynamic(output, attributes)
#    return parsing    

if __name__ == '__main__':
    full_pth = os.path.join(os.getcwd(), "templates")
    with open('devices.yaml') as f:
        devices = yaml.safe_load(f)
    print(send_and_parse_show_command(devices[1], 'sh ip int br', full_pth))