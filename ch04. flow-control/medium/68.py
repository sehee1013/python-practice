total = 0

# 전략: 메뉴 함수 출력, while 반복문으로 메뉴 추가, 종료 시 합계 출력 

# 조건: 메뉴 번호 입력 반복, 해당 메뉴의 번호를 입력한 경우
# 동작: 메뉴 추가 메시지 출력, 금액 total에 추가
# 탈출: 입력값이 0인 경우, 반복 종료 후 합계 출력

menu_dict = {
    1: ("아메리카노" ,4000),
    2: ("카페라떼" ,4500),
    3: ("녹차" ,3500)
}
def menu():
    print("--- 메뉴 ---")
    print(f"1. {menu_dict[1][0]} ({menu_dict[1][1]}원)")
    print(f"2. {menu_dict[2][0]} ({menu_dict[2][1]}원)")
    print(f"3. {menu_dict[3][0]} ({menu_dict[3][1]}원)")
    print("0. 주문 완료")

while True:
    menu()
    menu_num = int(input())
    # 0일 때만 종료이므로 not in menu_dict 사용 불가
    if menu_num == 0:
        print(f"총 주문 금액: {total}원")
        break
    elif menu_num in menu_dict:
        total += menu_dict[menu_num][1]
        print(f"{menu_dict[menu_num][0]}를 추가했습니다.")