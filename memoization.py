"""Мемоизация результатов функции с помощью декоратора."""

from functools import wraps
from typing import Any, Callable, Dict, Tuple, Type, TypeVar


Result = TypeVar("Result")
TypedValue = Tuple[Type[Any], Any]
CacheKey = Tuple[Tuple[TypedValue, ...], Tuple[Tuple[str, Type[Any], Any], ...]]


def memoize(function: Callable[..., Result]) -> Callable[..., Result]:
    """Сохраняет результат функции для каждого набора аргументов."""
    cache: Dict[CacheKey, Result] = {}

    @wraps(function)
    def wrapper(*args: Any, **kwargs: Any) -> Result:
        typed_args = tuple((type(value), value) for value in args)
        typed_kwargs = tuple(
            sorted((name, type(value), value) for name, value in kwargs.items())
        )
        key = (typed_args, typed_kwargs)
        try:
            hash(key)
        except TypeError as error:
            raise TypeError("Аргументы функции должны быть хешируемыми") from error

        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]

    return wrapper


@memoize
def fibonacci(number: int) -> int:
    """Вычисляет число Фибоначчи и запоминает готовые результаты."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError("Номер должен быть целым числом")
    if number < 0:
        raise ValueError("Номер не может быть отрицательным")
    if number < 2:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


def main() -> None:
    """Считывает номер и печатает соответствующее число Фибоначчи."""
    try:
        number = int(input("Номер числа Фибоначчи: "))
    except ValueError:
        print("Ошибка: нужно ввести целое число")
        return

    try:
        print(fibonacci(number))
    except (TypeError, ValueError) as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
