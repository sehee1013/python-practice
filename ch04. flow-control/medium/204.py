# 콜라츠 추측 과정과 횟수를 출력하세요.
num = int(input())
count = 0

# n이 1이 될 때까지 반복
while True:
    # 과정 출력
    print(num)
    
    # 탈출
    if num == 1:
        break
    # 짝수인 경우 // 2
    if num % 2 == 0:
        num //= 2
    # 홀수면 * 3 + 1
    else:
        num = num * 3 + 1

    count += 1

# 결과 출력
print(f"횟수: {count}")