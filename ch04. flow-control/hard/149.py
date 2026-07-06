# while True와 if/elif로 구현하세요.
borrowed = 0
max_books = 5

# menu가 4가 아닌 동안 계속 반복
while True:
    # 메뉴판 출력
    print("===== 도서관 대출 시스템 =====")
    print("1. 대출")
    print("2. 반납")
    print("3. 대출현황 조회")
    print("4. 종료")
    
    menu = int(input())

    # menu가 1인 경우: 0권 이하, 대출 한도 순으로 판별
    if menu == 1:
        new_borrow = int(input())
        if new_borrow <= 0:
            print("1권 이상 입력해 주세요.")
        elif new_borrow + borrowed > max_books:
            print(f"대출 한도 초과! 추가 대출 가능 권수: {max_books - borrowed}권")
        else:
            borrowed += new_borrow
            print(f"{new_borrow}권을 대출했습니다. (현재 대출: {borrowed}권)")
    # menu가 2인 경우: 현재 대출 권수, 0권 이하, 대출 한도 순으로 판별
    elif menu == 2:
        if borrowed == 0:
            print("현재 대출한 도서가 없습니다.")
        else:
            return_book = int(input())
            if return_book <= 0:
                print("1권 이상 입력해 주세요.")
            elif return_book > borrowed:
                print(f"대출 권수보다 많이 반납할 수 없습니다. (현재 대출: {borrowed}권)")
            else:
                borrowed -= return_book
                print(f"{return_book}권을 반납했습니다. (현재 대출: {borrowed}권)")
    # menu가 3인 경우: 대출 현황 출력
    elif menu == 3:
        print(f"현재 대출 권수: {borrowed}권")
        print(f"추가 대출 가능: {max_books - borrowed}권")
    # menu가 4인 경우: 감사 메시지 출력 후 종료
    elif menu == 4:
        print("이용해 주셔서 감사합니다.")
        break
    # 그 외: 재선택 경고 메시지 출력
    else:
        print("잘못된 메뉴입니다. 다시 선택해 주세요.")
    
    print() # 빈 줄 출력으로 시각적 구분 