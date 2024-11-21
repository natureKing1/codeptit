def chuyen(n):
    code=[]
    cnt=1
    for i in range(1,len(n)):
        if n[i]==n[i-1]:
            cnt+=1
        else:
            code.append(str(cnt))
            code.append(n[i-1])
            cnt=1
    code.append(str(cnt))
    code.append(n[-1])
    return "".join(code)
t=int(input())
for _ in range(t):
    n=input()
    print(chuyen(n))

