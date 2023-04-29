#!/bin/python3

import sys


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_prime_factor = n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            other_factor = n // i
            if is_prime(other_factor):
                max_prime_factor = other_factor
                break
            elif is_prime(i):
                max_prime_factor = i
    print(max_prime_factor)
