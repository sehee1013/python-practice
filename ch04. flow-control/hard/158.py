# 정답 317. 자릿수 분리 후 각 자리 비교
answer_d1 = 3
answer_d2 = 1
answer_d3 = 7
attempt = 0

# 정답을 맞출 때까지 반복
while True:
    # strike, ball 변수 선언해서 매반복마다 구해주기
    strike = 0
    ball = 0

    # 숫자 입력 받기
    guess = int(input())
    # 시도횟수 + 1
    attempt += 1
    
    # 자릿수 구하기
    guess_d1 = guess // 100
    guess_d2 = (guess // 10) % 10
    guess_d3 = guess % 10

    # ===== 자릿수 별 스트라이크, 볼 판별 =====
    # 같은 숫자가 같은 자리에 있는 경우 strike + 1
    if guess_d1 == answer_d1:
        strike += 1

    # 같은 숫자가 다른 자리에 있는 경우 ball + 1
    elif guess_d1 == answer_d2 or guess_d1 == answer_d3:
        ball += 1

    # 같은 숫자가 같은 자리에 있는 경우 strike + 1
    if guess_d2 == answer_d2:
        strike += 1

    # 같은 숫자가 다른 자리에 있는 경우 ball + 1
    elif guess_d2 == answer_d1 or guess_d2 == answer_d3:
        ball += 1

    # 같은 숫자가 같은 자리에 있는 경우 strike + 1
    if guess_d3 == answer_d3:
        strike += 1

    # 같은 숫자가 다른 자리에 있는 경우 ball + 1
    elif guess_d3 == answer_d1 or guess_d3 == answer_d2:
        ball += 1

    # ===== 결과 출력 =====
    # 정답이면 정답 메시지, 시도횟수 출력 후 종료
    if strike == 3:
        print(f"{strike}스트라이크! 정답입니다!")
        print(f"총 {attempt}번 만에 맞추셨습니다!")
        break
    # strike, ball 둘 다 0이면 out 출력
    elif strike == 0 and ball == 0:
        print("아웃!")
    
    # 그 외: strike, ball 값 출력
    else:
        print(f"{strike}스트라이크 {ball}볼")