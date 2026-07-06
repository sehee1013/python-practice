mileage = 0
total_earned = 0
total_used = 0
rate = 5

def print_menu():
        print("===== 마일리지 시스템 =====")
        print("1. 구매 (마일리지 적립)")
        print("2. 마일리지 사용")
        print("3. 마일리지 조회")
        print("4. 종료")

# 동작 4번 아닌 경우 계속 반복
while True:
    # 메뉴판 출력 후 동작 번호 입력      
    print_menu()
    menu = int(input())

    # 동작 번호 1번인 경우: 구매 금액 입력 후 양수 여부 판별, 마일리지 계산, 적립
    if menu == 1:
        price = int(input())
        if price <= 0:
            print("구매 금액은 양수여야 합니다.")
        else:
            earned = (price * rate) // 100
            mileage += earned
            total_earned += earned
            print(f"{earned} 마일리지가 적립되었습니다!")
    # 동작 번호 2번인 경우: 보유 마일리지 0 이상 여부, 사용값 0 이하, 보유금 초과 여부 순으로 판단 후 사용 후 사용 마일리지 차감
    elif menu == 2:
        if mileage <= 0:
            print("보유 마일리지가 없습니다.")
        else:
            use_earned = int(input())
            if use_earned <= 0:
                print("1 이상의 값을 입력해 주세요.")
            elif use_earned > mileage:
                print(f"마일리지가 부족합니다. (보유: {mileage})")
            else:
                total_used += use_earned
                mileage -= use_earned
                print(f"{use_earned} 마일리지를 사용했습니다.")
                print(f"남은 마일리지: {mileage}")
    # 동작 번호 3번인 경우: 보유 마일리지 출력, 총 적립 & 총 사용 출력
    elif menu == 3:
        print(f"보유 마일리지: {mileage}")
        print(f"총 적립: {total_earned} / 총 사용: {total_used}")
    # 동작 번호 4번인 경우: 이용 감사 메시지 출력 후 종료
    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break
    # 그 외: 경고 메시지 출력
    else:
        print("잘못된 메뉴입니다.")
    # 빈 줄 출력으로 시각적 구분
    print()