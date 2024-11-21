def tong(num):
    return sum(ord(digit)-ord('0') for digit in str(num))

def countStep(num):
    steps=0
    if num<10:
        return 1
    while num>=10:
        num=tong(num)
        steps+=1
    return steps
n=int(input())
print(countStep(n))