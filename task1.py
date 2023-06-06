# from cmath import sqrt
import math


def frequency_bitwise_test(sequence: list) -> float:
    return math.erfc((sum(sequence)/math.sqrt(len(sequence)))/math.sqrt(2))
