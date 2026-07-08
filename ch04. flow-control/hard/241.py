# 숫자로 채운 모래시계 패턴을 출력
n = int(input())

# 줄어드는 정도 discount = min(row, N - 1 - row)
# 출력 숫자 범위: discount + 1부터 N - discount 까지
# 앞 공백: 2 * discount

# 총 n줄 출력
for row in range(n):
    # 각 행의 출력 숫자 개수만큼 반복
    discount = min(row, n - 1 - row)
    # 공백 출력
    print(" " * 2 * discount, end="")

    for num in range(discount + 1, n - discount + 1):
        # 숫자 출력
        print(num, end=" ")
    print()