import math

# 1부터 N 사이의 완전제곱수를 출력하세요.
N = int(input())

# 1부터 루트N 까지 정수 i * i 출력
for i in range(1, math.isqrt(N) + 1):
    print(i * i)