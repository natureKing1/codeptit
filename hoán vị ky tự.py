from itertools import permutations
s=input()
b=permutations(s)
for i in b:
    print("".join(i))