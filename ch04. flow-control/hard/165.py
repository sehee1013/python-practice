goal = 10
pos = 0
step_count = 0

# 전략: 1 또는 2를 입력 받음, 입력 받은 숫자만큼 pos에 더함, 
#       pos값만큼 "#"출력, 나머지 "-". 입력 받을 때마다 step_count +1

# 메뉴얼 출력
print("=== 계단 오르기 ===")
print("목표:", goal, "칸")
print("1칸(1) 또는 2칸(2)을 선택하여 올라가세요!")
print() #빈 줄 출력으로 시각적 구분

while True:
    # 골에 도달하면 축하 메시지 출력 후 종료
    if pos == goal:
        print() #빈 줄 출력하여 시각적 구분
        print(f"축하합니다! 총 {step_count}번 만에 계단을 올랐습니다!")
        break
    # 이동값 입력 받기
    move_step = int(input())
    # 입력 값이 1 또는 2가 아닌 경우 경고 메시지 출력
    if move_step == 1:
        # 입력 값 pos에 더하고 pos값만큼 "#"출력, 나머지는 "-"출력
        pos += 1
        step_count += 1
        # 이동 현황과 이동 횟수 출력
        print(f'[{"#" * pos + "-" * (goal - pos)}] {pos}/{goal}칸 ({step_count}번째 이동)')        
    elif move_step == 2:
        # 입력 값 pos에 더하고 pos값만큼 "#"출력, 나머지는 "-"출력
        pos += 2
        step_count += 1
        # 이동 현황과 이동 횟수 출력
        print(f'[{"#" * pos + "-" * (goal - pos)}] {pos}/{goal}칸 ({step_count}번째 이동)')

    else:
        print("1 또는 2를 입력하세요.")