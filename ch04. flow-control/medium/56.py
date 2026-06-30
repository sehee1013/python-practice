# while True 안에서 메뉴를 먼저 출력한 뒤 input()으로 선택을 받으세요.
# 메뉴 딕셔너리
responses = {
    "1" : "안녕하세요!",
    "2" : "오늘 날씨가 좋습니다!"
}

while True:
    # 메뉴 출력
    print("===== 메뉴 =====")
    print("1. 인사")
    print("2. 날씨")
    print("q. 종료")
    print("=" * 16)

    choice = input().strip()
    if choice == "q": #q 입력한 경우 프로그램 종료
        print("프로그램을 종료합니다")
        break
    elif choice in responses:
        # 입력값에 대한 메시지 출력
        print(responses[choice])
    # 그 외는 잘못된 입력
    else:
        print("잘못된 입력입니다")