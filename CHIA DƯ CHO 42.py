a=[]
while len(a)<10:
    x=list(map(int,input().split()))
    for i in x:
        a.append(i)
new=set(n%42 for n in a )

print(len(new))



