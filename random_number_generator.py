"""Генератор случайных целых чисел в заданном диапазоне."""

from random import Random
from typing import Iterator, Optional


def random_numbers(
    start: int,
    end: int,
    count: int,
    generator: Optional[Random] = None,
) -> Iterator[int]:
    """Генерирует указанное количество чисел от start до end включительно."""
    values = {"Начало диапазона": start, "Конец диапазона": end, "Количество": count}
    for name, value in values.items():
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} должно быть целым числом")

    if start > end:
        raise ValueError("Начало диапазона не может быть больше конца")
    if count < 0:
        raise ValueError("Количество не может быть отрицательным")

    source = generator if generator is not None else Random()
    for _ in range(count):
        yield source.randint(start, end)


def read_integer(prompt: str) -> int:
    """Считывает целое число с понятным сообщением об ошибке."""
    try:
        return int(input(prompt))
    except ValueError as error:
        raise ValueError("нужно ввести целое число") from error


def main() -> None:
    """Считывает границы диапазона и печатает случайные числа."""
    try:
        start = read_integer("Начало диапазона: ")
        end = read_integer("Конец диапазона: ")
        count = read_integer("Количество чисел: ")
        print(*random_numbers(start, end, count))
    except (TypeError, ValueError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
