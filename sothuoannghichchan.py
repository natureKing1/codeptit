def kt(n):
    s = str(n)
    return s == s[::-1] and all(int(c) % 2 == 0 for c in s)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        res = []
        for x in range(22, n, 2):

            if len(str(x)) % 2 == 0 and kt(x):
                res.append(x)
        print(" ".join(map(str, res)))