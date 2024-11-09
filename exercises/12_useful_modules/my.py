# -*- coding: utf-8 -*-
'''
Скрипт для проверки работы всех функций из предыдущих заданий вместе
'''
from task_12_1 import ping_ip_addresses as pg
from task_12_2 import convert_ranges_to_ip_list as cv
from task_12_3 import print_ip_table as pr

ip_list = ['8.8.4.4', '1.1.1.1-2', '172.21.41.128-172.21.41.129']
pr(pg(cv(ip_list)))
