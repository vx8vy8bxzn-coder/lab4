"""Вычисление квадратов чисел от 1 до 10 с помощью map."""

from typing import List


def squares_from_one_to_ten() -> List[int]:
    """Возвращает квадраты целых чисел от 1 до 10."""
    return list(map(lambda number: number**2, range(1, 11)))


def main() -> None:
    """Печатает полученные квадраты чисел."""
    print(*squares_from_one_to_ten())


if __name__ == "__main__":
    main()
