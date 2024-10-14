'''Задача 2. Работа с текущим временем и датой
Напишите скрипт, который получает текущее время и дату, а затем выводит их в
формате YYYY-MM-DD HH:MM:SS. Дополнительно, выведите день недели и номер недели в году.'''

from datetime import datetime


def display_current_datetime():
    now = datetime.now()

    formatter_data = now.strftime('%Y-%m-%d %H:%M:%S')
    day_of_week = now.strftime('%A')
    week_num = now.isocalendar()[1]
    print(f'Текущая дата и время: {formatter_data}')
    print(f'День недели: {day_of_week}')
    print(f'Номер недели: {week_num}')

if __name__ == '__main__':
    display_current_datetime()