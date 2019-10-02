#!/bin/python3

def sum_digits(arr):
    
    mod = list(map(lambda x: abs(x) % 10, arr))
    div = list(map(lambda x: abs(x) // 10, arr))
    som = mod

    while list(filter(lambda x: x != 0, div)):
        mod = list(map(lambda x: x % 10, div))
        div = list(map(lambda x: x // 10, div))
        som = list(map(lambda x, y: x + y, som, mod))
    return som


def test():
    print(sum_digits([0,0,0,0,0,0,0]))
    print(sum_digits([1.2,1.55,0,280,32,2.6666,1]))
    print(sum_digits([5846,123456789,3256,2002.666]))
    print(sum_digits([0.2,0.0003,5,0.012,3,22,11]))
    print(sum_digits([-55,-25,-3,2.5,-2,-23,-10]))

test()
