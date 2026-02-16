"""
Модуль для генерації унікальних випадкових чисел для лотереї.
"""

import random


def get_numbers_ticket(min, max, quantity):
    """
    Генерує набір унікальних випадкових чисел для лотереї.

    Args:
        min (int): Мінімальне можливе число у наборі (не менше 1).
        max (int): Максимальне можливе число у наборі (не більше 1000).
        quantity (int): Кількість чисел, які потрібно вибрати.

    Returns:
        list: Відсортований список унікальних випадкових чисел.
              Повертає порожній список, якщо параметри не відповідають обмеженням.

    Обмеження:
        - min >= 1
        - max <= 1000
        - min <= max
        - quantity повинна бути в межах від 1 до (max - min + 1)

    Examples:
        >>> numbers = get_numbers_ticket(1, 49, 6)
        >>> len(numbers)
        6
        >>> all(1 <= n <= 49 for n in numbers)
        True
        >>> len(numbers) == len(set(numbers))  # перевірка унікальності
        True
    """
    # Перевірка валідності вхідних параметрів

    # Перевірка типів даних
    if not all(isinstance(param, int) for param in [min, max, quantity]):
        return []

    # Перевірка діапазону min та max
    if min < 1 or max > 1000:
        return []

    # Перевірка, що min не більше max
    if min > max:
        return []

    # Перевірка кількості: повинна бути додатньою і не більшою за можливий діапазон
    available_numbers = max - min + 1
    if quantity < 1 or quantity > available_numbers:
        return []

    # Генерація унікальних випадкових чисел
    # random.sample гарантує унікальність чисел
    lottery_numbers = random.sample(range(min, max + 1), quantity)

    # Сортування результату
    lottery_numbers.sort()

    return lottery_numbers


# Приклади використання
if __name__ == "__main__":
    print("=" * 60)
    print("Генератор лотерейних чисел")
    print("=" * 60)

    # Приклад 1: Класична лотерея 6 з 49
    print("\n1. Лотерея 6 з 49:")
    lottery_numbers = get_numbers_ticket(1, 49, 6)
    print(f"   Ваші лотерейні числа: {lottery_numbers}")

    # Приклад 2: Лотерея 5 з 36
    print("\n2. Лотерея 5 з 36:")
    lottery_numbers = get_numbers_ticket(1, 36, 5)
    print(f"   Ваші лотерейні числа: {lottery_numbers}")

    # Приклад 3: Лотерея 10 з 90
    print("\n3. Лотерея 10 з 90:")
    lottery_numbers = get_numbers_ticket(1, 90, 10)
    print(f"   Ваші лотерейні числа: {lottery_numbers}")

    # Приклад 4: Невалідні параметри (quantity > діапазон)
    print("\n4. Тест з невалідними параметрами (quantity > діапазон):")
    lottery_numbers = get_numbers_ticket(1, 10, 15)
    print(f"   Результат: {lottery_numbers} (порожній список)")

    # Приклад 5: Невалідні параметри (min > max)
    print("\n5. Тест з невалідними параметрами (min > max):")
    lottery_numbers = get_numbers_ticket(50, 10, 5)
    print(f"   Результат: {lottery_numbers} (порожній список)")

    # Приклад 6: Невалідні параметри (min < 1)
    print("\n6. Тест з невалідними параметрами (min < 1):")
    lottery_numbers = get_numbers_ticket(0, 49, 6)
    print(f"   Результат: {lottery_numbers} (порожній список)")

    # Приклад 7: Невалідні параметри (max > 1000)
    print("\n7. Тест з невалідними параметрами (max > 1000):")
    lottery_numbers = get_numbers_ticket(1, 1001, 6)
    print(f"   Результат: {lottery_numbers} (порожній список)")

    # Приклад 8: Граничний випадок - вибрати всі числа в діапазоні
    print("\n8. Граничний випадок - вибрати всі числа (1-10, quantity=10):")
    lottery_numbers = get_numbers_ticket(1, 10, 10)
    print(f"   Результат: {lottery_numbers}")

    # Демонстрація унікальності при множинних викликах
    print("\n9. Демонстрація випадковості (3 виклики для лотереї 6 з 49):")
    for i in range(3):
        lottery_numbers = get_numbers_ticket(1, 49, 6)
        print(f"   Спроба {i+1}: {lottery_numbers}")

    print("\n" + "=" * 60)

