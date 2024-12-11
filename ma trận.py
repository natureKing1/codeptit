def cal(matrix, n, k):
    upper_sum = 0
    lower_sum = 0

    for i in range(n):
        for j in range(n):
            if i + j < n - 1:
                upper_sum += matrix[i][j]
            elif i + j > n - 1:
                lower_sum += matrix[i][j]
    dif = abs(upper_sum - lower_sum)
    if dif <= k:
        print("YES")
    else:
        print("NO")

    print(dif)
n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
k = int(input())
cal(matrix, n, k)