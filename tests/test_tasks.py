"""Проверки всех заданий варианта 9."""

import unittest
from random import Random
from typing import List

from data_pipeline import (
    keep_positive,
    process_data,
    sort_numbers,
    square_numbers,
)
from memoization import fibonacci, memoize
from prime_generator import is_prime, prime_numbers
from random_number_generator import random_numbers
from squares_with_map import squares_from_one_to_ten


class SquaresWithMapTests(unittest.TestCase):
    """Проверки вычисления квадратов через map."""

    def test_returns_squares_from_one_to_ten(self) -> None:
        self.assertEqual(
            squares_from_one_to_ten(),
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
        )

    def test_returns_new_list_for_each_call(self) -> None:
        first_result = squares_from_one_to_ten()
        second_result = squares_from_one_to_ten()

        self.assertIsNot(first_result, second_result)


class RandomNumberGeneratorTests(unittest.TestCase):
    """Проверки генератора случайных чисел."""

    def test_generates_requested_number_of_values(self) -> None:
        numbers = list(random_numbers(10, 20, 15, Random(5)))

        self.assertEqual(len(numbers), 15)
        self.assertTrue(all(10 <= number <= 20 for number in numbers))

    def test_seed_makes_result_repeatable(self) -> None:
        first = list(random_numbers(1, 100, 5, Random(42)))
        second = list(random_numbers(1, 100, 5, Random(42)))

        self.assertEqual(first, second)

    def test_equal_range_bounds_are_allowed(self) -> None:
        self.assertEqual(list(random_numbers(7, 7, 3)), [7, 7, 7])

    def test_zero_count_returns_empty_sequence(self) -> None:
        self.assertEqual(list(random_numbers(1, 5, 0)), [])

    def test_rejects_reversed_range(self) -> None:
        with self.assertRaises(ValueError):
            list(random_numbers(10, 1, 3))

    def test_rejects_negative_count(self) -> None:
        with self.assertRaises(ValueError):
            list(random_numbers(1, 10, -1))

    def test_rejects_boolean_arguments(self) -> None:
        with self.assertRaises(TypeError):
            list(random_numbers(True, 10, 3))


class PrimeGeneratorTests(unittest.TestCase):
    """Проверки генератора простых чисел."""

    def test_recognizes_prime_and_composite_numbers(self) -> None:
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(29))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(49))

    def test_generates_primes_up_to_limit(self) -> None:
        self.assertEqual(
            list(prime_numbers(30)),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
        )

    def test_small_limit_returns_empty_sequence(self) -> None:
        self.assertEqual(list(prime_numbers(1)), [])

    def test_rejects_negative_limit(self) -> None:
        with self.assertRaises(ValueError):
            list(prime_numbers(-1))

    def test_rejects_non_integer_limit(self) -> None:
        with self.assertRaises(TypeError):
            list(prime_numbers(10.5))


class DataPipelineTests(unittest.TestCase):
    """Проверки последовательной обработки данных."""

    def test_applies_all_steps_in_order(self) -> None:
        result = process_data(
            [-3, 4, 2, -1, 3],
            keep_positive,
            square_numbers,
            sort_numbers,
        )

        self.assertEqual(result, [4, 9, 16])

    def test_accepts_generator_as_input(self) -> None:
        data = (number for number in [-2, 1, 3])

        self.assertEqual(process_data(data, keep_positive), [1, 3])

    def test_without_steps_returns_list_copy(self) -> None:
        original = [3, 1, 2]
        result = process_data(original)

        self.assertEqual(result, original)
        self.assertIsNot(result, original)

    def test_rejects_non_callable_step(self) -> None:
        with self.assertRaises(TypeError):
            process_data([1, 2, 3], "не функция")


class MemoizationTests(unittest.TestCase):
    """Проверки декоратора мемоизации."""

    def test_reuses_saved_result(self) -> None:
        calls = []

        @memoize
        def multiply(first: int, second: int) -> int:
            calls.append((first, second))
            return first * second

        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(multiply(6, 7), 42)
        self.assertEqual(calls, [(6, 7)])

    def test_keyword_order_does_not_change_cache_key(self) -> None:
        calls = []

        @memoize
        def add(first: int, second: int) -> int:
            calls.append((first, second))
            return first + second

        self.assertEqual(add(first=2, second=3), 5)
        self.assertEqual(add(second=3, first=2), 5)
        self.assertEqual(len(calls), 1)

    def test_preserves_function_information(self) -> None:
        @memoize
        def example() -> str:
            """Описание функции."""
            return "готово"

        self.assertEqual(example.__name__, "example")
        self.assertEqual(example.__doc__, "Описание функции.")

    def test_rejects_unhashable_arguments(self) -> None:
        @memoize
        def count_values(values: List[int]) -> int:
            return len(values)

        with self.assertRaises(TypeError):
            count_values([1, 2, 3])

    def test_calculates_fibonacci_numbers(self) -> None:
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(10), 55)

    def test_rejects_invalid_fibonacci_number(self) -> None:
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(TypeError):
            fibonacci(True)


if __name__ == "__main__":
    unittest.main()
