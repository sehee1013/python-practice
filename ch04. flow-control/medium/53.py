# while True 안에서 음수면 break, 아니면 total에 누적.
total = 0

# 숫자 입력 받고 음수 입력되면 종료, 입력 받은 숫자 전부 합한 값 출력
while True:
    num = int(input())
    if num < 0:
        break
    total += num

# 제시된 출력 양식 우선해서 출력
print("합계:", total)