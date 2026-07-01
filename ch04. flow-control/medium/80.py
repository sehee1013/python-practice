n = int(input())
total = 0

# 1부터 입력받은 n값까지 더한 합기반복문 이용해서 출력하기
for num in range(1, n + 1):
    total += num

print(f"1부터 {n}까지의 합: {total}")