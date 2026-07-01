total = 0
count = 0
BREAK_NUM = 100

# 종료 전까지 계속 반복
while True:
    # 탈출: 누적합이 100을 넘는 순간 반복 종료
    if total > BREAK_NUM:
        break

    # 숫자 입력 받기
    num = int(input())
    # 입력 횟수 1 증가, 입력 받은 숫자 total에 더함
    count += 1
    total += num

# 100초과 메시지, 누적합과 입력 횟수 출력
print(f"누적합이 {BREAK_NUM}을 초과했습니다!")
print(f"누적합: {total}")
print(f"입력 횟수: {count}")