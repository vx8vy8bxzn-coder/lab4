"""Pipeline для последовательной обработки числовых данных."""

from typing import Callable, Iterable, List


PipelineStep = Callable[[List[int]], List[int]]


def process_data(data: Iterable[int], *steps: PipelineStep) -> List[int]:
    """Последовательно применяет переданные функции к данным."""
    result = list(data)
    for step in steps:
        if not callable(step):
            raise TypeError("Каждый шаг pipeline должен быть функцией")
        result = step(result)
    return result


def keep_positive(numbers: List[int]) -> List[int]:
    """Оставляет только положительные числа."""
    return list(filter(lambda number: number > 0, numbers))


def square_numbers(numbers: List[int]) -> List[int]:
    """Возводит каждое число в квадрат."""
    return list(map(lambda number: number**2, numbers))


def sort_numbers(numbers: List[int]) -> List[int]:
    """Сортирует числа по возрастанию."""
    return sorted(numbers)


def main() -> None:
    """Считывает числа и пропускает их через pipeline."""
    try:
        numbers = [
            int(value) for value in input("Введите числа через пробел: ").split()
        ]
    except ValueError:
        print("Ошибка: нужно вводить только целые числа")
        return

    result = process_data(numbers, keep_positive, square_numbers, sort_numbers)
    print(*result)


if __name__ == "__main__":
    main()
