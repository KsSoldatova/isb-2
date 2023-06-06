import math


def identical_consecutive_bits_test(sequence: list) -> float:
    xi = sum(sequence)/len(sequence)
    if (abs(xi - 0.5) > 2/math.sqrt(128)):
        return 0
    vn = 0
    for i in range(0, len(sequence)-1):
        if (sequence[i] != sequence[i+1]):
            vn += 1
    return math.erfc(abs(vn - 2 * len(sequence)*xi*(1 - xi)) / (2 * math.sqrt(2 * len(sequence)) * xi * (1 - xi)))
