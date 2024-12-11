import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return True

def check(n):
    if not isPrime(len(n)):
        return False
    cnt = 0
    for i in n:
        if isPrime(ord(i) - ord('0')):
            cnt += 1
    return cnt > len(n) - cnt

for i in range(int(input())):
    n = input()
    if check(n):
        print("YES")
    else:
        print("NO")