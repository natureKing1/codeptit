t=int(input())
for _ in range(t):
    x,y,x1,y1=map(float,input().split())
    res=((x-x1)**2+(y-y1)**2)**0.5
    print(f"{res:.4f}")
