#!/bin/python3

import sys


def max_product(n, k, num):
    num = str(num)
    max_product = 0
    for i in range(n):
        end = i + k
        if end < n:
            product = 1
            for j in range(i, end):
                product *= int(num[j])
            if product > max_product:
                max_product = product
    return max_product


t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    print(max_product(n, k, num))