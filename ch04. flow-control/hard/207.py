# 정답: 37
# 스트라이크, 볼, 스트라이크 + 볼 == 0이면 아웃 
# 전략: 
    # 1. 입력 받은 값 // 10 해서 10의 자리 수(몫) 구함. 
    # 2. 몫이 3이면 스트라이크 + 1, 몫이 7이면 볼 + 1 
    # 3. 입력 받은 값 % 10 해서 1의 자리 수(나머지) 구함.
    # 4. 나머지가 7이면 스트라이크 + 1, 3이면 볼 + 1
    # 5. 결과 출력 후 정답 아니면 계속 반복 
# 탈출: 정답을 맞추면(스트라이크 == 2) 반복 종료 후 시도 회수 출력

ANSWER_VALUE = 37
answer_tens = ANSWER_VALUE // 10 
answer_ones = ANSWER_VALUE % 10
try_count = 0

while True:
    guess_value = int(input())
    try_count += 1

    strike = 0
    ball = 0

    # 정답 메시지 출력 후 반복 종료
    if guess_value == ANSWER_VALUE:
        print(f"정답! {try_count}번 만에 맞춤")
        break
    
    # 10의 자리 판정(스트라이크인 경우, 볼인 경우)
    if guess_value // 10 == answer_tens:
        strike += 1
    elif guess_value // 10 == answer_ones:
        ball += 1
    
    # 1의 자리 판정
    if guess_value % 10 == answer_ones:
        strike += 1
    elif guess_value % 10 == answer_tens:
        ball += 1
    
    # 결과 판정
    if strike + ball == 0:
        print("아웃")
    else:
        print(f"{strike}스트라이크 {ball}볼")