total = 0

# 조건: 1부터 100까지 반복
# 동작: 홀수만 total에 더함
# 결과: total값 출력

for num in range(1, 101):
    if num % 2 != 0:
        total += num
        
print(f"1부터 100까지 홀수의 합: {total}")