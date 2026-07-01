num = int(input())
total = 0

# num이 0보다 클 때까지 반복
while num > 0:
    # num을 10으로 나눴을 때의 나머지 total에 더하기
    total += num % 10
    # num을 10으로 나눴을 때의 몫을 num에 대입
    num = num // 10

# 결과 출력
print(f"각 자릿수의 합: {total}")