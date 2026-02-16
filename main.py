"""
Головний модуль для демонстрації виконання завдань.
"""

from task1 import get_days_from_today
from task2 import get_numbers_ticket


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


if __name__ == '__main__':
    main()
