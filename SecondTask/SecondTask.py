from typing import Callable
import re

def generator_numbers(text: str):
    pattern = r" (\d+\.\d+) "
    for match in re.finditer(pattern, text):
        yield float(match.group(1))

def sum_profit(text: str, func: Callable):
    gen = func(text)
    total = sum(gen)
    return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")