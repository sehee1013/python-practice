# 거래 종류를 판별하여 잔액을 관리하세요.
balance = int(input())

# 3번 동안 입력 받기
for _ in range(3):

    # 거래 메뉴 입력 받기
    menu = input()
    # 입력값 공백 기준으로 나눠서 리스트 저장
    menu_list = menu.split()
    
    # 요소 0번째 값이 "입금"인 경우
    if menu_list[0] == "입금":
        # 잔액에 요소 1번째 값 잔액에 더해서 잔액 갱신
        balance += int(menu_list[1])
        print(f"입금 완료: 잔액 {balance}원")

    # 요소 0번째 값이 "출금"인 경우
    elif menu_list[0] == "출금":
        # 잔액 부족하면 실패 메시지 출력
        if balance < int(menu_list[1]):
            print("출금 실패: 잔액 부족")
        else:
            # 잔액에 요소 1번째 값 잔액에 빼서 잔액 갱신
            balance -= int(menu_list[1])
            print(f"출금 완료: 잔액 {balance}원")

    # 요소 0번째 값이 "조회"인 경우
    elif menu_list[0] == "조회":
        # 잔액 출력
        print(f"현재 잔액: {balance}원")

# 최종 잔액 출력
print(f"최종 잔액: {balance}원")