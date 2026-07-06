# while True, if/elif로 구현
last_issued = 0
last_called = 0
# 종료 전까진 계속 반복
while True:
    # 메뉴판 출력 후 동작 번호 입력
    print("===== 은행 대기번호 =====")
    print("1. 번호 발급")
    print("2. 다음 고객 호출")
    print("3. 대기인원 확인")
    print("4. 종료")
    menu = int(input())
    # 1번인 경우: 대기 번호 발급, 대기 인원 수 + 1
    if menu == 1:
        last_issued += 1
        print(f"대기번호 {last_issued}번이 발급되었습니다.")
    # 2번인 경우: 대기 인원 수 판별, 대기 번호 호출, 대기 인원 수 - 1
    elif menu == 2:
        if last_issued - last_called <= 0:
            print("대기 중인 고객이 없습니다.")
        else:
            last_called += 1
            print(f"{last_called}번 고객님, 오세요!")
    # 3번인 경우: 대기 인원 수 출력
    elif menu == 3:
        print(f"현재 대기인원: {last_issued - last_called}명")
    # 4번인 경우: 종료 메시지 출력 후 종료
    elif menu == 4:
        print("시스템을 종료합니다.")
        break
    # 잘못된 번호인 경우: 경고 메시지 출력
    else:
        print("잘못된 메뉴입니다.")
    # 빈 줄 출력으로 시각적 구분
    print()
