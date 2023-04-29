#!/bin/python3

import sys

def ap_sum(a_1, a_N, N):
    # In the derivation, N will always be even(account for the zero if N is odd) 
    # and thus shall never be a floating number. Thus floor division is used to remove the decimal part
    return ((a_1 + a_N) * N)//2

def num_multiples_sum(num, n):
    N = (n - 1)//num  # Only sum up mulitples LESS THAN n
    a_1 = num
    a_N = N * num
    return ap_sum(a_1, a_N, N)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    three_mutiples_sum = num_multiples_sum(3, n)
    five_multiples_sum = num_multiples_sum(5, n)
    fifteen_multiples_sum = num_multiples_sum(15, n)
    total = three_mutiples_sum + five_multiples_sum - fifteen_multiples_sum
    print(total)