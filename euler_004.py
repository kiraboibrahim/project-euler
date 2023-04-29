
def is_palindrome(v):    
    v = str(v)
    return v == v[::-1] 


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    max_palindrome = 101101
    for i in range(100, 1000):
        for j in range(100, 1000):
            prod = i * j
            if prod > max_palindrome and prod < n and is_palindrome(prod):
                max_palindrome = prod
    print(max_palindrome)
