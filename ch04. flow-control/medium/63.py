# i==0 또는 i==n-1 또는 j==0 또는 j==n-1 이면 테두리입니다.
n = int(input())

# n만큼 행 출력, 1번째와 n번째 행은 * n개 출력
for row in range(n):
    if row == 0 or row == n - 1:
        print("*" * n)
    # 나머지 행은 처음과 마지막에 * 출력, 그 사이에는 공백 출력
    else:
        print(f"*{' ' * (n - 2)}*")       