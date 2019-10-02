#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the winningLotteryTicket function below.
def winningLotteryTicket(tickets,n):
    winner = []
    for i in range(n):
        for j in range(i):
            if i != j:
                concatenateTickets = "".join([tickets[i],tickets[j]])
                for m in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    if m not in list(concatenateTickets):
                        break
                if m == '9':
                    winner.append([i, j])
    
    return len(winner)

def test(n):
    for _ in range(n):
        tickets_item = str(random.randint(1,10**6))
        tickets.append(tickets_item)

    print(winningLotteryTicket(tickets,n))
    print(winningLotteryTicket(['1293455', '5559948277', '12334556', '56789', '123456879'], 5))
    print(winningLotteryTicket(['129300455', '5559948277', '012334556', '56789', '123456879'], 5))

if __name__ == '__main__':
    tickets = []
    n = int(input("Quantos tickets serão inseridos? "))
    test(n)