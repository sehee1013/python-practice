# 모래시계 패턴을 출력하세요.
n = int(input())

# 가운데 행을 기준으로 감소, 증가
# 첫 번째 행 "*" n개 출력 점차 2개씩 줄어듦
# 공백 0개 출력 점차 1개씩 늘어남
for star in range(n, 0, -2):
    empty = (n - star) // 2
    print(" " * empty + "*" * star)

# 가운데 행(n // 2 + 1) "*" 1개 출력 후 다시 2개씩 늘어남
for star in range(3, n + 1, 2):
    empty = (n - star) // 2
    print(" " * empty + "*" * star)