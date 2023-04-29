#!/bin/python3

import sys
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_min_multiple(n):
    com_multiple = 2 if n >= 2 else 1
    primes = [2]
    for num in range(3, n+1):
        if is_prime(num):
            com_multiple *= num
            primes.append(num)
        elif com_multiple % num != 0:
            tmp = num
            is_divisible = False
            for prime in primes:
                # Prime factorize the number(num) until the common multiple is divisible by the number(num) 
                while tmp % prime == 0 and not is_divisible:
                    com_multiple *= prime
                    if com_multiple % num == 0:
                        is_divisible = True
                        break
                    tmp //= prime
                if is_divisible:
                    break
    return com_multiple
             

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(get_min_multiple(n))