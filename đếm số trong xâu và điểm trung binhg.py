t=int(input())
res=[]
for _ in range(t):
    s=input()
    n=input()
    bdau=0
    cnt=0
    while 1:
        found_n=s.find(n,bdau)
        if found_n==-1:break
        cnt+=1
        bdau=found_n+len(n)
    res.append(cnt)
for x in res:
    print(x)


n=int(input())
lst=list(map(float,input().split()))
min_s=min(lst)
max_s=max(lst)
loc_lst=[score for score in lst if score!=min_s and score!= max_s]
average=sum(loc_lst)/len(loc_lst)
print(f"{average:.2f}")




