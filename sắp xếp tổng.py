def total(n):
    total=0
    while n!=0:
        total+=n%10
        n//=10
    return total
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.sort(key=total)
    print(*a)

def accumulation(n):
    accumulation=1
    while n!=0:
        accumulation*=n%10
        n//=10
    return accumulation
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    a.sort(key=accumulation)
    print(*a)
