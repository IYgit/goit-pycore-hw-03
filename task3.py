"""
Модуль для нормалізації телефонних номерів до стандартного формату.
"""

import re


def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до стандартного формату.

    Функція видаляє всі символи крім цифр та '+', та додає міжнародний код '+38'
    для України, якщо він відсутній.

    Args:
        phone_number (str): Рядок з телефонним номером у будь-якому форматі.

    Returns:
        str: Нормалізований телефонний номер у форматі '+380XXXXXXXXX'.

    Правила нормалізації:
        - Видаляються всі символи крім цифр та '+'
        - Якщо номер починається з '+380', залишається як є
        - Якщо номер починається з '380', додається '+'
        - Якщо номер починається з '0', '380' замінює '0'
        - Інші номери отримують префікс '+38'

    Examples:
        >>> normalize_phone("    +38(050)123-32-34")
        '+380501233234'
        >>> normalize_phone("     0503451234")
        '+380503451234'
        >>> normalize_phone("(050)8889900")
        '+380508889900'
        >>> normalize_phone("38050-111-22-22")
        '+380501112222'
    """
    # Видаляємо всі символи крім цифр та '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)

    # Обробка різних варіантів формату
    if cleaned_number.startswith('+'):
        # Номер вже має '+', перевіряємо чи є код країни
        if cleaned_number.startswith('+380'):
            # Номер вже в правильному форматі
            return cleaned_number
        elif cleaned_number.startswith('+38'):
            # Номер має '+38', але можливо неповний код
            return cleaned_number
        elif cleaned_number.startswith('+80'):
            # Помилково вказано +80 замість +380
            return '+3' + cleaned_number[1:]
        else:
            # Інший міжнародний код - залишаємо як є
            return cleaned_number
    elif cleaned_number.startswith('380'):
        # Номер має код 380, але без '+'
        return '+' + cleaned_number
    elif cleaned_number.startswith('80'):
        # Номер починається з 80 (можливо без 3)
        return '+3' + cleaned_number
    elif cleaned_number.startswith('0'):
        # Номер у локальному форматі (починається з 0)
        return '+38' + cleaned_number
    else:
        # Номер без коду країни та без початкового 0
        return '+38' + cleaned_number


# Приклади використання
if __name__ == "__main__":
    print("=" * 70)
    print("Нормалізація телефонних номерів для SMS-розсилки")
    print("=" * 70)

    # Тестові дані з завдання
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

    print("\nВхідні номери:")
    print("-" * 70)
    for i, num in enumerate(raw_numbers, 1):
        print(f"{i}. '{num}'")

    print("\nНормалізовані номери:")
    print("-" * 70)
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

    for i, (original, normalized) in enumerate(zip(raw_numbers, sanitized_numbers), 1):
        print(f"{i}. '{original.strip()}' -> '{normalized}'")

    print("\nСписок нормалізованих номерів для SMS-розсилки:")
    print(sanitized_numbers)

    # Додаткові тести
    print("\n" + "=" * 70)
    print("Додаткові тести:")
    print("=" * 70)

    additional_tests = [
        ("050 123 45 67", "Локальний формат з пробілами"),
        ("+38 (050) 123-45-67", "Повний формат з символами"),
        ("38(050)123-45-67", "Без + на початку"),
        ("  +380501234567  ", "З пробілами на початку та в кінці"),
        ("0501234567", "Простий локальний формат"),
        ("+38050-123-45-67", "З дефісами"),
    ]

    for phone, description in additional_tests:
        normalized = normalize_phone(phone)
        print(f"  {description}:")
        print(f"    '{phone}' -> '{normalized}'")

    print("\n" + "=" * 70)

