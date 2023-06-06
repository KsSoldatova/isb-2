import math
import scipy


def the_longest_units_sequence_test(sequence: list) -> float:
    v = [0, 0, 0, 0]
    pi = [0.2148, 0.3672, 0.2305, 0.1875]
    i = j = 0
    while i < 128:
        count = 1
        longest = 1
        while j < i + 7:
            change = False
            if (sequence[j]):
                if (sequence[j] == sequence[j+1]):
                    if (not change):
                        count += 1
                    else:
                        change = False
                else:
                    change = True
                    if (count > longest):
                        longest = count

                        tmp = sequence[j]
                    count = 1
            j += 1
        if (count > longest):
            longest = count
        if (longest <= 1):
            v[0] += 1
        elif (longest == 2):
            v[1] += 1
        elif (longest == 3):
            v[2] += 1
        elif (longest >= 4):
            v[3] += 1
        i = j
        i += 1
        j += 1
    xi = sum(list(map(lambda x, y: math.pow((x - 16*y), 2)/(16*y), v, pi)))
    return scipy.special.gammaincc(1.5, xi/2)
