# 각 줄에서 이항계수를 누적 곱으로 계산하세요.
n = int(input())

# 각 행을 순서대로 출력
for row in range(n):
    # 공백: n - 1 - row개 출력
    print(" " * (n - 1 - row), end="")
    
    # 항상 첫 시작 숫자는 1
    num = 1
    print(num, end=" ")

    # 줄 번호만큼 숫자 출력
    for col in range(row):
        
        # 다음 값 = 이전 값 * (줄 번호 - col) // (col + 1)
        num = num * (row - col) // (col + 1)

        print(num, end=" ")
    # 줄바꿈
    print()