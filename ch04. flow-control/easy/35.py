n = int(input())
total = 0

# 1부터 num까지 합 구하기, 합계 출력 
for num in range(1, n + 1):
    total += num

print("1부터", n, "까지의 합:", total)