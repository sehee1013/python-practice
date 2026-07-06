# while True, if/elif로 메뉴 분기 후 break 처리
price1 = 1200
price2 = 1500
price3 = 2000
qty1 = 0
qty2 = 0
qty3 = 0

# 유효 입력 후 1을 입력하는 동안은 계속 반복
while True:
    # 메뉴판 출력, 상품 선택
    print("===== 편의점 =====")
    print(f"1. 삼각김밥 ({price1}원)")
    print(f"2. 음료수 ({price2}원)")
    print(f"3. 과자 ({price3}원)")
    menu = int(input())
    # 상품 선택 후 수량 입력, 상품 당 총 가격 계산
    if menu == 1:
        new_order_1 = int(input())
        qty1 += new_order_1
        print(f"삼각김밥 {new_order_1}개 추가!")
    elif menu == 2:
        new_order_2 = int(input())
        qty2 += new_order_2
        print(f"음료수 {new_order_2}개 추가!")
    elif menu == 3:
        new_order_3 = int(input())
        qty3 += new_order_3
        print(f"과자 {new_order_3}개 추가!")
    # 상품 번호 외 숫자 입력 시, 경고 메시지 출력
    else:
        print("잘못된 상품 번호입니다.")
        continue
    # 계속 쇼핑을 진행할 경우 1 입력, 그 외는 break하고 총액 출력
    keep_going = int(input())
    if keep_going != 1:
        break
    # 빈 줄 출력으로 시각적 구분
    print()
# 반복 종료 후 계산서 출력
print() #빈 줄 출력으로 시각적 구분
print("===== 계산서 =====")
if qty1 > 0:
    print(f"삼각김밥 x {qty1} = {price1 * qty1}원")
if qty2 > 0:
    print(f"음료수 x {qty2} = {price2 * qty2}원")
if qty3 > 0:
    print(f"과자 x {qty3} = {price3 * qty3}원")

print(f"총액: {(price1 * qty1) + (price2 * qty2) + (price3 * qty3)}원")