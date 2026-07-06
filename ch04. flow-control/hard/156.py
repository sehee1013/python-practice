# if/elif로 모드 분기 후 while로 변경 과정 출력
current_temp = int(input())
target_temp = int(input())


# 현재 온도 == 목표 온도 : 종료
if current_temp == target_temp:
    print("이미 목표 온도입니다.")

elif current_temp < target_temp: # 현재 온도 < 목표 온도: 난방 모드, 1도씩 올리며 도달 시 목표 온도 T도에 도달 시 도달 완료 메시지 출력
    print("난방 모드를 시작합니다.")
    while current_temp != target_temp:
        print(f"현재 온도: {current_temp}도 → {current_temp + 1}도")
        current_temp += 1
    print(f"목표 온도 {target_temp}도에 도달했습니다!")
else: # 현재 온도 > 목표 온도: 냉방 모드, 1도씩 내리며 도달 시 목표 온도 T도에 도달 시 도달 완료 메시지 출력
    print("냉방 모드를 시작합니다.")
    while current_temp != target_temp:
        print(f"현재 온도: {current_temp}도 → {current_temp - 1}도")
        current_temp -= 1

    print(f"목표 온도 {target_temp}도에 도달했습니다!")