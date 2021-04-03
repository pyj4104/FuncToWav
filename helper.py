from extended_int import int_inf
from typing import Callable

def heaviside(x: int, start: int, end: int = int_inf):
    if x >= start and x <= end:
        return 1
    else:
        return 0

def combineFuncs(a: Callable, b: Callable) -> Callable:
    return lambda x: a(x) + b(x)
