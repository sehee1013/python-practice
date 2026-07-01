money = int(input())
# 음료 가격 딕셔너리
drink_dict = {
    1 : {"name":"물", "fee":500},
    2 : {"name":"주스", "fee":1000},
    3 : {"name":"커피", "fee":1500},
}
# 음료 목록 함수 
def drink_list():
    print(f"1. {drink_dict[1]['name']} ({drink_dict[1]['fee']}원)")
    print(f"2. {drink_dict[2]['name']} ({drink_dict[2]['fee']}원)")
    print(f"3. {drink_dict[3]['name']} ({drink_dict[3]['fee']}원)")

# 잔액이 500원 이상이면 반복
while True:
    # 잔액이 500원 미만되면 종료
    if money < 500:
        break
    # 잔액과 음료 목록 출력
    print(f"잔액: {money}원")
    drink_list()
    # 음료 선택 입력 받기
    drink_choice = int(input())
    # 선택이 1/2/3이 아니면 경고 메시지 출력, 잔액 차감 X
    if drink_choice in drink_dict:
        # 유효한 선택 후 잔액 >= 가격이면 잔액 차감 후 메시지 출력
        if money >= drink_dict[drink_choice]['fee']:
            money -= drink_dict[drink_choice]['fee']
            print(f"{drink_dict[drink_choice]['name']}를 선택했습니다.")
        # 잔액 부족할시 메시지 출력 후 종료
        else:
            print("잔액이 부족합니다.")
            break
    else: 
        print("잘못된 선택입니다.")

# 남은 금액 출력
print(f"남은 금액: {money}원")