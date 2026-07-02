answer = 42
tries = 0
print("=== 숫자 맞추기 게임 (1~100) ===")

# 맞출 때까지 반복
while True:

    # guess 입력 받고 시도 횟수 + 1
    guess = int(input())
    tries += 1
    
    # 정답이면 정답 메시지, 시도 횟수 출력 후 종료
    if guess == answer:
        print(f"정답입니다! 시도 횟수: {tries}번")
        break
    # guess가 정답보다 크면 down
    elif guess > answer:
        print("DOWN!")
    # guess가 정답보다 작으면 up
    else:
        print("UP!")