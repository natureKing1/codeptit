for i in range(int(input())):
    s=input().split()
    ans=s[0]
    for t in s[1:]:
        if len(ans)+len(t)+1>100:
            break
        ans+=" "+ t
    print(ans)
