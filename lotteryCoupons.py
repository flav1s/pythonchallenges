#!/bin/python3
import math
import os
import random
import re
import sys

def lotteryCoupons(n):
    if n == 0: # caso o numero de cupons inserido for 0, retorna 0
        return 0
        
    coupons = range(1, n+1) # vetor coupons
    # map: Serve para aplicar uma função a cada elemento de uma lista, retornando uma nova lista contendo os elementos resultantes da aplicação da função.
    # lambda: função arbitrária
    # filter: Filtra os elementos de uma sequência
    couponsMod = list(map(lambda x: abs(x) % 10, coupons)) 
    couponsDiv = list(map(lambda x: abs(x) // 10, coupons))
    couponsSum = couponsMod

    while list(filter(lambda x: x != 0, couponsDiv)): # enquanto existir valores em couponsDiv que forem diferentes de 0, o loop continua.
        # filter() só “deixa passar” para a sequência resultante aqueles elementos para os quais a chamada da função que o usuário passou retornar True.
        couponsMod = list(map(lambda x: x % 10, couponsDiv))
        couponsDiv = list(map(lambda x: x // 10, couponsDiv))
        couponsSum = list(map(lambda x, y: x + y, couponsSum, couponsMod))

    maxCouponsSum = max(couponsSum) # maior valor de 
    #winnersCount = list(map(lambda x: couponsSum.count(x), range(1, maxCouponsSum +1)))    
    winnersCount = [] # inicializa a lista
    for i in range(1, maxCouponsSum + 1): # range de 1 até o maior valor do cupom
        winnersCount.append(couponsSum.count(i)) # lista com a quantidade de vezes que cada valor de cupom aparece 

    maxWinnerCount = max(winnersCount) # maior valor da lista winnersCount, ou seja, maior quantidade de vencedores no sorteio
    s = winnersCount.count(maxWinnerCount) # quantas vezes o maior valor de winnersCount aparece na lista
    return s


def test():
    for i in range(0,23):
        print(lotteryCoupons(i))

if __name__ == '__main__':
    test()