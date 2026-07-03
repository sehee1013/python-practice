height = int(input())

# 기준 키 상수 설정
PASS = 130
PASS_WITHOUT_GUARDIAN = 150

# 탑승: 키 130 이상 -> 보호자 동반 여부 -> 키 150 이상(보호자 없는 경우) 순으로 확인
# 키 130 넘는지 확인 후 안 넘으면 탑승 불가, 넘으면 보호자 여부 확인
if height >= PASS:
    is_guardian = input().strip()
    if is_guardian == "Y":
        print("보호자와 함께 탑승 가능합니다.")
    else:
        # 보호자 없는 경우 키 150 이상이면 탑승 가능 미만이면 보호자 필요 메시지 출력
        if height >= PASS_WITHOUT_GUARDIAN:
            print("혼자 탑승 가능합니다.")
        else:
            print("보호자가 필요합니다.")
else:
    print("탑승할 수 없습니다.")