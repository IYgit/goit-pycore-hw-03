"""
Головний модуль для демонстрації виконання завдань.
"""

from datetime import datetime
from task1 import get_days_from_today
from task2 import get_numbers_ticket
from task3 import normalize_phone
from task4 import get_upcoming_birthdays


def main():
    """Демонстрація роботи всіх завдань."""

    print("=" * 70)
    print("ЗАВДАННЯ 1: Розрахунок днів від заданої дати до поточної")
    print("=" * 70)

    # Приклад використання task1
    print("\nПриклади використання get_days_from_today():")
    print(f"  Від '2020-10-09' до сьогодні: {get_days_from_today('2020-10-09')} днів")
    print(f"  Від '2027-12-31' до сьогодні: {get_days_from_today('2027-12-31')} днів")

    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 2: Генератор лотерейних чисел")
    print("=" * 70)

    # Приклад використання task2
    print("\nПриклади використання get_numbers_ticket():")
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(f"  Лотерея 6 з 49: {lottery_numbers}")

    lottery_numbers = get_numbers_ticket(1, 36, 5)
    print(f"  Лотерея 5 з 36: {lottery_numbers}")

    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 3: Нормалізація телефонних номерів")
    print("=" * 70)

    # Приклад використання task3
    print("\nПриклади використання normalize_phone():")
    raw_numbers = [
        "067\t123 4567",
        "(095) 234-5678\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]

    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print(f"  Нормалізовані номери телефонів для SMS-розсилки:")
    for i, (original, normalized) in enumerate(zip(raw_numbers, sanitized_numbers), 1):
        print(f"    {i}. '{original.strip()}' -> '{normalized}'")

    print("\n" + "=" * 70)
    print("ЗАВДАННЯ 4: Привітання з днем народження")
    print("=" * 70)

    # Приклад використання task4
    today = datetime.today().date()
    print(f"\nПоточна дата: {today.strftime('%Y.%m.%d')}")
    print("\nПриклади використання get_upcoming_birthdays():")

    # Приклад з завдання
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"}
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print(f"\n  Список привітань на цьому тижні:")
    if upcoming_birthdays:
        for item in upcoming_birthdays:
            print(f"    - {item['name']}: {item['congratulation_date']}")
    else:
        print("    Немає днів народження на наступні 7 днів")

    print("\n" + "=" * 70)


if __name__ == '__main__':
    main()
