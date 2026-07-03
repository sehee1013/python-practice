n = int(input())

print(f"{n}의 약수:", end = " ")
# 숫자 N 나눠서 약수 구해서 출력하기
for divisor in range(1, n + 1):
    if n % divisor == 0:
        print(divisor, end = " ")