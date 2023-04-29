#!/bin/python3

import sys

def ap_sum(a_1, a_N, N):
    # In the derivation, N will always be even(account for the zero if N is odd) 
    # and thus shall never be a floating number. Thus floor division is used to remove the decimal part
    return ((a_1 + a_N) * N)//2


def natural_square_sum(n):
    return (n *(n+1) * (2*n + 1))//6


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ap_sum_ = ap_sum(1, n, n)
    squaure_sum = natural_square_sum(n)
    result = (ap_sum_**2) - squaure_sum
    print(result)
