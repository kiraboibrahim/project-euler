#!/bin/python3

import sys

def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

memory = {1: 2, "last_computed_pos": 1}

def get_nth_prime(n):
    global memory
    if n in memory:
        return memory[n]
    pos = 1
    curr_prime = 2
    odd_idx = 1
    curr_odd = (2*odd_idx) + 1
    last_computed_pos = memory["last_computed_pos"]
    if n > last_computed_pos:
        pos = last_computed_pos
        curr_prime = memory[pos]
        odd_idx = ((curr_prime - 1)//2) + 1
        curr_odd = (2*odd_idx) + 1
    while pos < n:
        if is_prime(curr_odd):
            curr_prime = curr_odd
            pos += 1
            memory[pos] = curr_prime
        odd_idx += 1
        curr_odd = (2*odd_idx) + 1
    memory["last_computed_pos"] = n
    return curr_prime



t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    nth_prime = get_nth_prime(n)
    print(nth_prime)
