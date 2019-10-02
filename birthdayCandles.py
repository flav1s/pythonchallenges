#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(candles, nCandles):
    if nCandles == 0 or nCandles != len(candles):
        return 0

    biggestCandle = max(candles)
    if biggestCandle >= 0:
        numberCandles = candles.count(biggestCandle)
    else:
        return 0

    return numberCandles


def test():
    candles = []
    nCandles = 4
    for _ in range(nCandles):
        candles_item = random.randint(1,9)
        candles.append(candles_item)
    print(birthdayCakeCandles(candles, nCandles))
    print(birthdayCakeCandles([4,4,5,2,3], 5))
    print(birthdayCakeCandles([3,3,3,3], 4))
    print(birthdayCakeCandles([2,2,3,5,5,5,5], 7))
    print(birthdayCakeCandles([], 0))
    print(birthdayCakeCandles([1], 1))
    print(birthdayCakeCandles([-5,-2], 2))


if __name__ == '__main__':
    test()