# -*- coding: utf-8 -*-

"""
Задание 22.2b

Скопировать класс CiscoTelnet из задания 22.2a и добавить метод send_config_commands.


Метод send_config_commands должен уметь отправлять одну команду конфигурационного
режима и список команд.
Метод должен возвращать вывод аналогичный методу send_config_set у netmiko
(пример вывода ниже).

Пример создания экземпляра класса:
In [1]: from task_22_2b import CiscoTelnet

In [2]: r1_params = {
   ...:     'ip': '192.168.100.1',
   ...:     'username': 'cisco',
   ...:     'password': 'cisco',
   ...:     'secret': 'cisco'}

In [3]: r1 = CiscoTelnet(**r1_params)

Использование метода send_config_commands:

In [5]: r1.send_config_commands('logging 10.1.1.1')
Out[5]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#logging 10.1.1.1\r\nR1(config)#end\r\nR1#'

In [6]: r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255'])
Out[6]: 'conf t\r\nEnter configuration commands, one per line.  End with CNTL/Z.\r\nR1(config)#interface loop55\r\nR1(config-if)#ip address 5.5.5.5 255.255.255.255\r\nR1(config-if)#end\r\nR1#'

"""

import telnetlib
import time
from textfsm import clitable

class CiscoTelnet:
    def __init__(self, ip, username, password, secret):
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self._write_line(username)
        self.telnet.read_until(b"Password:")
        self._write_line(password)
        self.telnet.read_until(b">")
        self._write_line("enable")
        self.telnet.read_until(b"Password:")
        self._write_line(secret)
        self.telnet.read_until(b"#")
        self._write_line("terminal length 0")
        time.sleep(1)
        self.telnet.read_very_eager().decode("utf-8")
        
    def _write_line(self, line):
        self.telnet.write(line.encode("utf-8") + b"\n")
        
    def send_show_command(self, command, parse=True, templates="templates", index="index"):
        self._write_line(command)
        output = self.telnet.read_until(b"#", timeout=1).decode("utf-8")
        if parse:
            return self._parse(output, command, index, templates)
        else:
            return output
    
    def _parse(self, command_output, command, index_file = "index", templ_path = "templates"):
        attributes_dict = {'Command': command}
        cli_table = clitable.CliTable(index_file, templ_path)
        cli_table.ParseCmd(command_output, attributes_dict)
        data_rows = [dict(zip(cli_table.header,row)) for row in cli_table]
        return data_rows
    
    def send_config_commands(self, commands):
        self._write_line("conf t")
        if type(commands) == list:
            for i in commands:
                self._write_line(i)
        else:
            self._write_line(commands)       
        self._write_line("end")
        time.sleep(1)
        output = self.telnet.read_very_eager().decode("utf-8")
        return output
    
if __name__ == '__main__':
    r1_params = {
        'ip': '192.168.100.1',
        'username': 'cisco',
        'password': 'cisco',
        'secret': 'cisco'}
    r1 = CiscoTelnet(**r1_params)
    print(r1.send_config_commands(['interface loop55', 'ip address 5.5.5.5 255.255.255.255']))