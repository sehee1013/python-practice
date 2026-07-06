parked = 0
max_cars = 10
total_income = 0
rate = 1000

# menu가 4가 아닌 동안 반복
while True:
    # 메뉴판 출력
    print("===== 주차장 관리 =====")
    print("1. 입차")
    print("2. 출차")
    print("3. 현황 조회")
    print("4. 종료")
    menu = int(input())
    # menu가 1인 경우: 만차인지 판별
    if menu == 1:
        if parked == max_cars:
            print("주차장이 만차입니다!")
        else:
            parked += 1
            print(f"차량이 입차되었습니다. (현재 주차: {parked}/{max_cars}대)")
    # menu가 2인 경우: 주차된 차 유무, 시간 입력 후 요금 계산, 최종 요금 출력
    elif menu == 2:
        if parked == 0:
            print("주차된 차량이 없습니다.")
        else:
            parked_time = int(input())
            parked -= 1
            fee = max(0, parked_time) * rate
            total_income += fee
            print(f"주차 요금: {fee}원")
            print(f"차량이 출차되었습니다. (현재 주차: {parked}/{max_cars}대)")
    # menu가 3인 경우: 현재 주차 수, 빈자리, 총 수입 출력
    elif menu == 3:
        print(f"현재 주차: {parked}/{max_cars}대")
        print(f"빈 자리: {max_cars - parked}대")
        print(f"총 수입: {total_income}원")
    # menu가 4인 경우: 종료 메시지 출력 후 종료
    elif menu == 4:
        print("시스템을 종료합니다.")
        break
    # 그 외: 잘못된 메뉴
    else:
        print("잘못된 메뉴입니다.")
    # 빈 줄 출력으로 시각적 구분
    print()