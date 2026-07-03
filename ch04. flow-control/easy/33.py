total = 0

# 홀수는 생략하고 짝수만 더해서 합계 출력
for num in range(1, 20 + 1):
    if num % 2 != 0:
        continue
    total += num
print(f"1~20 짝수 합계: {total}")