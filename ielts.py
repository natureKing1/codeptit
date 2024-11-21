

def ielts(n):
    if 39 <= n <= 40:
        return 9.0
    if 37 <= n <= 38:
        return 8.5
    if 35 <= n <= 36:
        return 8.0
    if 33 <= n <= 34:
        return 7.5
    if 30 <= n <= 32:
        return 7.0
    if 27 <= n <= 29:
        return 6.5
    if 23 <= n <= 26:
        return 6.0
    if 20 <= n <= 22:
        return 5.5
    if 16 <= n <= 19:
        return 5.0
    if 13 <= n <= 15:
        return 4.5
    if 10 <= n <= 12:
        return 4.0
    if 7 <= n <= 9:
        return 3.5
    if 5 <= n <= 6:
        return 3.0
    if 3 <= n <= 4:
        return 2.5
    return 1.0


T = int(input())

for _ in range(T):

    reading_correct, listening_correct, speaking_score, writing_score = map(float, input().strip().split())

    reading_score = ielts(float(reading_correct))
    listening_score = ielts(float(listening_correct))

    total_score = (reading_score + listening_score + speaking_score + writing_score) / 4

    if total_score % 1 < 0.25:
        overall_score = int(total_score)
    elif total_score % 1 < 0.75:
        overall_score = int(total_score) + 0.5
    else:
        overall_score = int(total_score) + 1.0

    print(overall_score)



