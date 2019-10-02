#!/bin/python3

import os
import sys
import random

#
# Complete the simpleArraySum function below.
#
def simpleArraySum(ar, nArr):
    soma = 0
    for i in range(nArr):
        soma = soma + ar[i]
    
    return soma
    

def test():
    ar = []
    nArr = 4
    for _ in range(nArr):
        arr_item = random.randint(1,100)
        ar.append(arr_item)
    print(simpleArraySum(ar, nArr))
    print(simpleArraySum([2.2, 2, 3, 5, 5.2], 5))
    print(simpleArraySum([1, 1, 1], 3))
    print(simpleArraySum([0], 1))
    print(simpleArraySum([-2, -4], 2))


if __name__ == '__main__':
    test()
