from itertools import combinations
n,k=map(int,input().split())
arr=list(map(int,input().split()))
arr2=sorted(set(arr))
res=combinations(arr2,k)
for i in res:
    print(*i)