# 컴퓨터 패턴: 1,2,3,1,2 (라운드별)
com_r1 = 1
com_r2 = 2
com_r3 = 3
com_r4 = 1
com_r5 = 2
player_wins = 0
com_wins = 0
round_num = 1

# 가위바위보 딕셔너리 생성
rock_scissors_paper = {1:"가위", 2:"바위", 3:"보" }

# 출력 함수 생성
def print_result() :
    print(f"[라운드 {round_num}]")
    print(f"나: {rock_scissors_paper[player]} vs 컴퓨터: {rock_scissors_paper[com]} → {result}")
    print(f"(현재 스코어) 나 {player_wins} : {com_wins} 컴퓨터")
    print()

print("=== 가위바위보 5판 3선승 ===")
print()

# 먼저 3승 하거나 5라운드 끝나면 종료
while True:
    result = ""
    # 입력 5번 받기
    player = int(input())

    # round 1, 4일 때 승패 판별
    if round_num == 1:
        com = com_r1
        if player == 1:
            result = "무승부"
        elif player == 2:
            result = "승리!"
            player_wins += 1
        else:
            result = "패배..."
            com_wins += 1

    # round 2일 때 승패 판별
    elif round_num == 2:
        com = com_r2
        if player == 1:
            result = "패배..."
            com_wins += 1
        elif player == 2:
            result = "무승부"
        else:
            result = "승리!"
            player_wins += 1

    # round 3일 때 승패 판별
    elif round_num == 3:
        com = com_r3
        if player == 1:
            result = "승리!"
            player_wins += 1
        elif player == 2:
            result = "패배..."
        else:
            result = "무승부"

    # round 4 일 때 승패 판별
    if round_num == 4:
        com = com_r4
        if player == 1:
            result = "무승부"
        elif player == 2:
            result = "승리!"
            player_wins += 1
        else:
            result = "패배..."
            com_wins += 1

    # round 5일 때 승패 판별
    elif round_num == 5:
        com = com_r5
        if player == 1:
            result = "패배..."
            com_wins += 1
        elif player == 2:
            result = "무승부"
        else:
            result = "승리!"
            player_wins += 1
    
    print_result()

    # 3승 또는 round 5일 때 종료
    if round_num == 5 or player_wins == 3:
        break
    round_num += 1

# 최종 결과 출력
if player_wins > com_wins:
    print(f"나의 승리! ({player_wins}:{com_wins})")
elif player_wins < com_wins:
    print(f"컴퓨터의 승리! ({player_wins}:{com_wins})")
else:
    print(f"무승부! ({player_wins}:{com_wins})")