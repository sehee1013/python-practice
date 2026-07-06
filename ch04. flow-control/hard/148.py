# while True와 if/elif로 메뉴 분기를 구현
balance = 100000
withdraw_limit = 500000


# 입력한 메뉴 번호가 4가 아닌 동안은 계속 반복
while True:
    # 메뉴 창 출력
    print("===== ATM =====")
    print("1. 입금")
    print("2. 출금")
    print("3. 잔액조회")
    print("4. 종료")
    menu = int(input())    

    # 1이면 입금 처리, 양수 여부 판별
    if menu == 1:
        deposit_amount = int(input())
        if deposit_amount <= 0:
            print("입금액은 양수여야 합니다.")
        else:
            balance += deposit_amount
            print(f"{deposit_amount}원이 입금되었습니다.")
            print(f"현재 잔액: {balance}원")
    # 2이면 출금 처리, 양수 여부 -> 한도 초과 -> 잔액 부족 순으로 판별
    elif menu == 2:
        withdraw_amount = int(input())
        if withdraw_amount <= 0:
            print("출금액은 양수여야 합니다.")
        elif withdraw_amount > withdraw_limit:
            print(f"1회 출금 한도({withdraw_limit}원)를 초과했습니다.")
        elif withdraw_amount > balance:
            print(f"잔액이 부족합니다. 현재 잔액: {balance}원")
        else:
            balance -= withdraw_amount
            print(f"{withdraw_amount}원이 출금되었습니다.")
            print(f"현재 잔액: {balance}원")
    # 3이면 잔액 조회 처리
    elif menu == 3:
        print(f"현재 잔액: {balance}원")
    # 4이면 이용 감사 메시지 출력 후 종료
    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break
    # 1~4가 아닌 숫자를 누른 경우 재선택 경고 메시지 출력
    else:
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")
    print() # 빈 줄 출력으로 시각적 분리