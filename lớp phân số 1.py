import math
#1
n,a=map(int,input().split())
gcd=math.gcd(n,a)
n_1=n//gcd
a_1=a//gcd
print(f'{n_1}/{a_1}')
#2
import math
n, a, n1, a1 = list(map(int, input().split()))
numerator_sum = n * a1 + n1 * a
denominator_sum = a * a1
gcd_sum = math.gcd(numerator_sum, denominator_sum)
numerator_sum //= gcd_sum
denominator_sum //= gcd_sum
print(f'{numerator_sum}/{denominator_sum}')