round_num = 1
streak = 0
best_streak = 0
total_correct = 0
total_games = 0
result = ""

coins_front_back = {
    1:"앞",
    2:"뒤"
}

def case_1_correct(input_value, streak, result, total_correct):
        if input_value == 1:
            streak += 1
            result = "정답!"
            total_correct += 1
        elif input_value == 2:
            result = "틀렸습니다!"
            streak = 0

        return streak, result, total_correct

def case_2_correct(input_value, streak, result, total_correct):
        if input_value == 2:
            streak += 1
            result = "정답!"
            total_correct += 1
        elif input_value == 1:
            result = "틀렸습니다!"
            streak = 0
        
        return streak, result, total_correct

# 게임 설명 메뉴 출력
print("=== 동전 뒤집기 게임 ===")
print("앞(1) 또는 뒤(2)를 맞춰보세요! (종료: 0)")
print()

# 0이 입력될 때까지 반복
while True:
    # 입력 받기
    input_value = int(input())
    # 0 입력되면 종료
    if input_value == 0:
        break

    # 총 게임수 추가
    total_games += 1

    # result 초기화하여 매 판 새로운 결과 출력
    result = ""
    # 3의 배수 라운드는 결과 반전
    if round_num % 3 == 0:
        # 짝수인 경우
        if round_num % 2 == 0:
            # 사용자의 입력값이 1이면 정답
            streak, result, total_correct = case_1_correct(input_value, streak, result, total_correct)            
        # 홀수인 경우
        else:
            streak, result, total_correct = case_2_correct(input_value, streak, result, total_correct)

    # 3의 배수 라운드가 아닌 경우
    else:
        # 홀수 라운드인 경우: 앞
        if round_num % 2 != 0:
            # 사용자의 입력값이 1이면 정답
            streak, result, total_correct = case_1_correct(input_value, streak, result, total_correct)
            
        # 짝수 라운드인 경우: 뒤
        else:
            # 사용자의 입력값이 2이면 정답, 연속 + 1, 토탈 + 1
            streak, result, total_correct = case_2_correct(input_value, streak, result, total_correct)

    # 라운드 카운트
    round_num += 1
    # 연속 정답 수가 최대 연속 정답 수보다 크면 갱신 
    if best_streak < streak:
        best_streak = streak
    
    # 결과 출력
    print(f"동전: {coins_front_back[input_value]}! {result} (연속 {streak}회)")


# 최종 결과 출력
print()
print("=== 게임 결과 ===")
print(f"총 게임: {total_games}회")
print(f"정답: {total_correct}회")
print(f"최대 연속 정답: {best_streak}회")