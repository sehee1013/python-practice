n = int(input())

# 승패 카운트 변수
win_count = 0
lose_count = 0
draw_count = 0

# 컴퓨터 패턴 리스트 생성
computer = ["바위", "보", "가위"]
# 이기는 (플레이어, 컴퓨터) 쌍을 집합으로 정의
win_cases = {("가위", "보"), ("바위", "가위"), ("보", "바위")}

# n번동안 플레이어 선택 입력 받기 반복
for turn in range(n):
    # 플레이어 선택 입력 받기
    player = input()

    # 무승부인 경우
    if player == computer[turn % 3]:
        result = "무"
        draw_count += 1

    # 이기는 경우
    elif (player, computer[turn % 3]) in win_cases:
        result = "승"
        win_count += 1
    # 지는 경우
    else:
        result = "패"
        lose_count += 1
        
    # turn판 결과 출력
    print(f"{turn + 1}판: 플레이어({player}) vs 컴퓨터({computer[turn % 3]}) -> {result}")

# 전적 출력
print(f"전적: {win_count}승 {lose_count}패 {draw_count}무")