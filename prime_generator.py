"""Генератор простых чисел."""

from math import isqrt
from typing import Iterator


def is_prime(number: int) -> bool:
    """Проверяет, является ли целое число простым."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Число должно быть целым")
    if number < 2:
        return False

    return all(number % divisor != 0 for divisor in range(2, isqrt(number) + 1))


def prime_numbers(limit: int) -> Iterator[int]:
    """Генерирует простые числа, не превышающие limit."""
    if isinstance(limit, bool) or not isinstance(limit, int):
        raise TypeError("Граница должна быть целым числом")
    if limit < 0:
        raise ValueError("Граница не может быть отрицательной")

    for number in range(2, limit + 1):
        if is_prime(number):
            yield number


def main() -> None:
    """Считывает верхнюю границу и печатает простые числа."""
    try:
        limit = int(input("Простые числа до: "))
    except ValueError:
        print("Ошибка: нужно ввести целое число")
        return

    try:
        print(*prime_numbers(limit))
    except (TypeError, ValueError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
