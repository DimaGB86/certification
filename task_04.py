'''Задача 4. Опции и флаги
Напишите скрипт, который принимает два аргумента командной строки: число и
строку. Добавьте следующие опции:
    ● --verbose, если этот флаг установлен, скрипт должен выводить
    дополнительную информацию о процессе.
    ● --repeat, если этот параметр установлен, он должен указывать,
    сколько раз повторить строку в выводе.
'''

import argparse

parser = argparse.ArgumentParser('Скрипт для вывода строки с опциями.')
parser.add_argument('number', type=int, help='Число для демонстрации.')
parser.add_argument('text', type=str, help='Строка дял вывода.')

parser.add_argument('--verbose', action='store_true', help='Вывести дополнительную информацию о процессе')
parser.add_argument('--repeat', type=int, default=1, help='Количество повторений строки')

args = parser.parse_args()

if args.verbose:
    print(f"Получено число: {args.number}",
          f"Полученная строка: {args.text}",
          f"Повторять строку: {args.repeat} раз")

for _ in range(args.repeat):
    print(args.text)

