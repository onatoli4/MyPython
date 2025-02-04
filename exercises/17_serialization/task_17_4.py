# -*- coding: utf-8 -*-
"""
Задание 17.4

Создать функцию write_last_log_to_csv.

Аргументы функции:
* source_log - имя файла в формате csv, из которого читаются данные (mail_log.csv)
* output - имя файла в формате csv, в который будет записан результат

Функция ничего не возвращает.

Функция write_last_log_to_csv обрабатывает csv файл mail_log.csv.
В файле mail_log.csv находятся логи изменения имени пользователя. При этом, email
пользователь менять не может, только имя.

Функция write_last_log_to_csv должна отбирать из файла mail_log.csv только
самые свежие записи для каждого пользователя и записывать их в другой csv файл.
В файле output первой строкой должны быть заголовки столбцов,
такие же как в файле source_log.

Для части пользователей запись только одна и тогда в итоговый файл надо записать
только ее.
Для некоторых пользователей есть несколько записей с разными именами.
Например пользователь с email c3po@gmail.com несколько раз менял имя:
C=3PO,c3po@gmail.com,16/12/2019 17:10
C3PO,c3po@gmail.com,16/12/2019 17:15
C-3PO,c3po@gmail.com,16/12/2019 17:24

Из этих трех записей, в итоговый файл должна быть записана только одна - самая свежая:
C-3PO,c3po@gmail.com,16/12/2019 17:24

Для сравнения дат удобно использовать объекты datetime из модуля datetime.
Чтобы упростить работу с датами, создана функция convert_str_to_datetime - она
конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
Полученные объекты datetime можно сравнивать между собой.
Вторая функция convert_datetime_to_str делает обратную операцию - превращает
объект datetime в строку.

Функции convert_str_to_datetime и convert_datetime_to_str использовать не обязательно.

"""

import datetime
import csv

def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")
"""
def write_last_log_to_csv(source_log, output):
    result = {}
    with open(source_log) as src, open(output, 'w') as dst:
        reader = csv.reader(src)
        writer = csv.writer(dst)
        writer.writerow(next(reader))
        for row in reader:
            if result.get(row[1]):
                if convert_str_to_datetime(row[2]) > result.get(row[1])[0]:
                    result[row[1]] = [convert_str_to_datetime(row[2]), row[0]]
            else:
                result[row[1]] = [convert_str_to_datetime(row[2]), row[0]]
        for key, item in result.items():
             writer.writerow([item[1], key, convert_datetime_to_str(item[0])])   
    print(result) 
"""
def write_last_log_to_csv(source_log, output):
    with open(source_log) as src:
        data = list(csv.reader(src))
        headers = data[0]
    sort_by_date = sorted(data[1:], key=lambda x: convert_str_to_datetime(x[2]))
    result = {}
    for name, mail, date in sort_by_date:
        result[mail] = (name, mail, date)
    
    with open(output, 'w') as dst:
        writer = csv.writer(dst)
        writer.writerow(headers)
        for d in result.values():
            writer.writerow(d)

if __name__ == '__main__':
    write_last_log_to_csv('mail_log.csv', 'new_mail.csv')