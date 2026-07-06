# while True로 반복, if/elif로 경우 분기
current = 1

# 0 입력 전까지 반복
while True:
    # 현재 층 출력 후 이동할 층 입력, 범위 밖, 현재 층과 같은가 순으로 판별
    if current == -1:
        print("현재 층: B1층")
    else:
        print(f"현재 층: {current}층")

    move_to = int(input())
    if move_to == 0:
        print("엘리베이터를 종료합니다.")
        break
    elif move_to not in range(-1, 11):
        print("이동할 수 없는 층입니다.")
    elif move_to == current:
        print("이미 해당 층에 있습니다.")
    # 이동 가정 시작층 -> ... -> 목표층
    else:
        # 올라가는 경우, current가 B1인 경우
        if current < move_to:
            floors_dict = {} #딕셔너리 초기화로 이전 기록 지우기
            if current == -1:
                floors_dict[-1] = "B1층"
                for floor in range(1, move_to + 1):
                    floors_dict[floor] = f"{floor}층"
            else:
                for floor in range(current, move_to + 1):
                    floors_dict[floor] = f"{floor}층"
        # 내려가는 경우, move_to가 B1인 경우
        else:
            floors_dict = {} 
            if move_to == -1:
                for floor in range(current, 0, -1):
                    floors_dict[floor] = f"{floor}층"
               
                floors_dict[-1] = "B1층"
            else:
                for floor in range(current, move_to - 1, -1):
                    floors_dict[floor] = f"{floor}층"

        print(" → ".join(floors_dict.values()))
        if move_to == -1: # 도착 메시지 출력 후 현재 층 갱신
            print("B1층에 도착했습니다.")
        else:
            print(f"{move_to}층에 도착했습니다.")

        current = move_to
    print() #빈 줄 출력으로 시각적 구분    