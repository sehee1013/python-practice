n = int(input())
m = int(input())
total = 0

# 1부터 n 사이 M의 배수의 합을 출력
# 숫자가 1부터 n까지 반복
for num in range(1, n + 1):
    # 숫자가 m의 배수이면 total에 더함
    if num % m == 0:
        total += num

# 결과 출력
print(f"1부터 {n}까지 {m}의 배수의 합: {total}")