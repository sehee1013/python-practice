n = int(input())
result = 1

# 1부터 입력받은 숫자 n까지의 수 곱해서 출력
for i in range(1, n + 1):
    result *= i

print(str(n) + "! =", result) 