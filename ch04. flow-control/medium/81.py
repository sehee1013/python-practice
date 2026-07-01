# 전략: 카운팅 변수 선언, 1부터 n사이의 정수 중 짝수이면 카운팅 +1
n = int(input())
count = 0

# 조건: 1부터 n 사이의 정수만
# 행동: 짝수의 개수 카운팅
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
print(f"1부터 {n}까지 짝수의 개수: {count}")