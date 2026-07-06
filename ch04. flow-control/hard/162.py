# pos, score, moves, got_treasure로 관리
pos = 0
score = 0
moves = 0
trap1 = 3
trap2 = 7
treasure = 5
exit_pos = 9
got_treasure = 0
retry = False
trap1_is_alive = True
trap2_is_alive = True
treasure_is_alive = True

print("=== 1차원 미로 탈출 ===")
print(f"탈출구는 위치 {exit_pos}입니다. 함정을 피하고 보물을 찾으세요!")
# 탈출구에 도착할 때까지 반복
while True:

    # 1, 2 이외 입력으로 재입력하는 경우는 현재 위치 출력 안 함 
    if not retry:
        print(f"현재 위치: {pos}")

    retry = False

    # 방향 입력 받기
    direction = int(input())

    # 방향값이 1 또는 2가 아닌 경우
    if direction not in (1, 2):
        print("1 또는 2를 입력하세요.")
        retry = True
        continue
    
    # 기존 위치값 따로 저장
    pre_pos = pos

    # 1을 입력 받은 경우
    if direction == 1:
        pos -= 1

    # 2를 입력 받은 경우
    else:
        pos += 1
    
    # 위치가 범위를 넘어간 경우
    if pos < 0 or pos > 9:
        print("이동할 수 없습니다! (범위 초과)")
        retry = True
        # 위치 복원
        pos = pre_pos
        continue

    moves += 1
    
    # 탈출구에 도착하면 종료
    if pos == exit_pos:
        print("탈출구에 도달했습니다!")
        print(f"현재 위치: {pos}")
        break

    # 함정1에 처음 진입한 경우
    if pos == trap1 and trap1_is_alive:
        print("함정! 위치 0으로 되돌아갑니다!")
        pos = 0
        trap1_is_alive = False
    
    # 함정2에 처음 진입한 경우
    elif pos == trap2 and trap2_is_alive:
        print("함정! 위치 4로 되돌아갑니다!")
        pos = 4
        trap2_is_alive = False

    # 보물에 처음 진입한 경우
    elif pos == treasure and treasure_is_alive:
        print("보물 발견! 점수 +10!")
        treasure_is_alive = False
        score += 10

# 결과 출력
print(f"탈출 성공! 총 이동 횟수: {moves}, 점수: {score}")