# 테두리만 있는 삼각형 패턴을 출력하세요.
n = int(input())

# n행 출력할 때까지 반복
for i in range(n):
    # 첫 행은 가운데 출력
    if i == 0:
        print(" " * (n - 1) + "*")
    # 마지막 행은 별 (2*N-1)개 연속 출력
    elif i == n - 1:
        print("*" * (2 * n - 1))
    # 중간 행들은 양쪽 끝에만 별 출력, 안쪽은 공백
    else:
        left_space = n - i - 1
        inner_space = i * 2 - 1
        print(" " * left_space + "*" + " " * inner_space + "*")