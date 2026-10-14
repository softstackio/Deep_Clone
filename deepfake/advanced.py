import math


def power(base, exponent):
    return base ** exponent


def sqrt(value):
    if value < 0:
        raise ValueError("Cannot take square root of a negative number")
    return math.sqrt(value)


def percent(value, pct):
    return value * pct / 100
