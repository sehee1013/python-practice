# 1부터 N 사이의 친화수 쌍을 출력하세요.
N = int(input())

# 4부터 n 사이의 모든 수 순회
for num in range(4, N + 1):
    sum_of_a = 0
    # 자기 자신을 제외한 모든 약수의 합 구하기
    for divisor in range(1, num):
        if num % divisor == 0:
            sum_of_a += divisor
 
    # 그 합의 약수를 구해서 본래 수와 같으면 출력
    sum_of_b = 0
    for divisor in range(1, sum_of_a):
        if sum_of_a % divisor == 0:
            sum_of_b += divisor

    # num과 sum_of_a(num의 약수의 합)의 약수의 합이 같고, sum_of_a이 num보다 크고 N의 범위 안에 있으면 출력
    if num == sum_of_b and num < sum_of_a <= N:
        print(f"({num}, {sum_of_a})")