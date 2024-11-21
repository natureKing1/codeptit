def octal(n):
    a=int(n,2)
    octal=oct(a)[2:]
    return octal
a=input().strip()
print(octal(a))