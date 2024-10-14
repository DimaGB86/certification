'''Задача 3. Планирование задач
Напишите функцию, которая принимает количество дней от текущей даты и
возвращает дату, которая наступит через указанное количество дней. Дополнительно,
выведите эту дату в формате YYYY-MM-DD.
'''

from datetime import datetime, timedelta


def get_future_date(days_from_now):
    today = datetime.now()
    future_datee = today + timedelta(days=days_from_now)

    formatted_date = future_datee.strftime("%Y-%m-%d")
    return formatted_date


if __name__ == '__main__':
    print(get_future_date(1))
