#!/bin/python3
# -*- coding: utf-8 -*-

import math
import os
import random
import re
import sys

# Complete the lonelyinteger function below.
def lonelyinteger(a):
    newList = []
    lonelyNumber = a[0]
        
    for i in range(len(a)):
        newList.append(a[i])
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                newList.remove(a[j])
    lonelyNumber = newList[0]
    return lonelyNumber            

def test():
    print("O número solitario é: ", lonelyinteger([5.5, 2, 2, 3, 3])) # 5.5
    print("O número solitario é: ", lonelyinteger([2, 2, 5, 3, 3])) # 5
    print("O número solitario é: ", lonelyinteger([25, 25, 3, 5, 3, 5, 28, 28, 9])) # 9
    print("O número solitario é: ", lonelyinteger([25, 25, 3, 5, 3, 1, 5, 28, 28, 9, 9])) # 1
    print("O número solitario é: ", lonelyinteger([3])) #3

if __name__ == '__main__':

    #a = list(map(int, input("Digite um array: ").rstrip().split()))
    #result = lonelyinteger(a)
    #print(result)
    test()