# -*- coding: utf-8 -*-
"""
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
import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG)
logger = logging.getLogger("netmiko")

def send_and_parse_show_command(device_dict, command, templates_path):
    os.environ["NET_TEXTFSM"] = templates_path
    with ConnectHandler(**device_dict) as ssh:
#        regex = r'.+#'
#        ssh.send_command('edit running', expect_string=regex)
#        print(ssh.find_prompt())
        output = ssh.send_command(command, use_textfsm=True)
        return output

if __name__ == '__main__':
    full_pth = os.path.join(os.getcwd(), "templates")
    with open('devices.yaml') as f:
        device = yaml.safe_load(f)[0]
    print(send_and_parse_show_command(device, 'show arp-table', full_pth))
