import math
import numpy as np


def combinations(size, sample):
    top = math.factorial(size)
    bottom = math.factorial(size - sample) * math.factorial(sample)
    return top / bottom

if __name__ == '__main__':

    print()