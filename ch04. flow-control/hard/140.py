# 지그재그 패턴을 출력하세요.
n = int(input())
m = int(input())

num = 1

# 행 n개 출력
for row in range(1, n + 1):
    # 행이 짝수이면 \t 출력
    if row % 2 == 0:
        print(" " * 2 * m, end="")
    # 열 m개 출력
    for col in range(m):
        print(num, end=" ")
        num += 1
        
    print()