"""
Модуль для розрахунку кількості днів між заданою датою та поточною датою.
"""

from datetime import datetime


def get_days_start_from_today(date):
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    Args:
        date (str): Рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').

    Returns:
        int: Кількість днів від заданої дати до поточної.
             Якщо задана дата пізніша за поточну, результат буде від'ємним.

    Raises:
        ValueError: Якщо формат дати неправильний.

    Examples:
        >>> get_days_start_from_today("2021-10-09")  # якщо сьогодні 2021-05-05
        -157
    """
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()

        # Отримуємо поточну дату (без часу)
        today = datetime.today().date()

        # Розраховуємо різницю між поточною датою та заданою датою
        difference = today - given_date

        # Повертаємо різницю у днях як ціле число
        return difference.days

    except ValueError as e:
        raise ValueError(f"Неправильний формат дати. Очікується 'РРРР-ММ-ДД', отримано: '{date}'") from e
    except Exception as e:
        raise Exception(f"Помилка при обробці дати: {e}") from e


# Приклади використання
if __name__ == "__main__":
    print("Приклади використання функції get_days_from_today():\n")

    # Приклад 1: Дата в минулому
    try:
        result = get_days_start_from_today("2020-10-09")
        print(f"Від '2020-10-09' до сьогодні: {result} днів")
    except Exception as e:
        print(f"Помилка: {e}")

    # Приклад 2: Дата в майбутньому
    try:
        result = get_days_start_from_today("2027-12-31")
        print(f"Від '2027-12-31' до сьогодні: {result} днів (від'ємне значення, бо дата в майбутньому)")
    except Exception as e:
        print(f"Помилка: {e}")

    # Приклад 3: Сьогоднішня дата
    try:
        today_str = datetime.today().strftime('%Y-%m-%d')
        result = get_days_start_from_today(today_str)
        print(f"Від сьогодні до сьогодні: {result} днів")
    except Exception as e:
        print(f"Помилка: {e}")

    # Приклад 4: Неправильний формат (обробка винятку)
    try:
        result = get_days_start_from_today("09-10-2020")
        print(f"Результат: {result}")
    except ValueError as e:
        print(f"Помилка: {e}")

