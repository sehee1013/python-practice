# 무한 루프 안에서 0 입력 시 BYE 출력 후 break, 그 외는 범위별 분기 후 카운트.
business_count = 0
normal_count = 0
economy_count = 0
# 0 입력 되기 전까지 계속 반복
while True:
    # 입력 받기
    seat_num = int(input())
    # 입력 값이 0이면 탈출
    if seat_num == 0:
        print("BYE")
        break
    # 입력값 1 ~ 10이면 비즈니스석 예약 출력, 카운트 + 1
    elif 1 <= seat_num <= 10:
        business_count += 1
        print("비즈니스석 예약")
    # 입력값 11 ~ 20이면 일반석 예약 출력, 카운트 + 1
    elif 11 <= seat_num <= 20:
        normal_count += 1
        print("일반석 예약")
    # 입력값 21 ~ 30이면 이코노미석 예약 출력, 카운트 + 1
    elif 21 <= seat_num <= 30:
        economy_count += 1
        print("이코노미석 예약")
    # 그 외: 잘못된 좌석 메시지 출력
    else:
        print("잘못된 좌석")

total_count = business_count + normal_count + economy_count
# 총 예약 출력
print(f"총 예약: {total_count}건")