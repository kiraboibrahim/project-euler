import sys


def is_even(n):
    return n % 2 == 0


def fab_even_sum(n):
    i, j = 0, 1
    fab_even_sum = 0
    while (fab := i + j) < n:
        if is_even(fab) and fab < n:
            fab_even_sum += fab
        i, j = j, fab

    return fab_even_sum

t = 1 # int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(fab_even_sum(100))
