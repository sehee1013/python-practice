# 공백을 먼저 (n-i)개 출력한 뒤 별을 i개 출력하세요.
n = int(input())

# n번 행 출력하고 행은 공백 (n - i)개, 별 i개 출력
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)