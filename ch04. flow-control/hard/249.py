# 투입금액과 상품가격을 입력받아 거스름돈을 최소 동전으로 출력하세요.
money = int(input())
price = int(input())

# 투입 금액에서 상품 가격을 빼서 거스름돈 총액 구하기
change_amount = money - price

# 돈 부족한 경우
if change_amount < 0:
    print("잔액이 부족합니다.")

# 부족하지 않은 경우
else:
    # 거스름돈 총액 출력
    print(f"거스름돈: {change_amount}원")

    # 거스름돈이 있는 경우
    if change_amount > 0:
    
        # 잔돈 총액을 500으로 나눠 500원 동전 갯수 구하기
        coins_500 = change_amount // 500
        change_amount %= 500

        # 잔돈 총액을 100으로 나눠 100원 동전 갯수 구하기
        coins_100 = change_amount // 100
        change_amount %= 100

        # 잔돈 총액을 50으로 나눠 50원 동전 갯수 구하기
        coins_50 = change_amount // 50
        change_amount %= 50

        # 나머지에서 10원 동전 갯수 구하기
        coins_10 = change_amount // 10

        # 결과 출력
        if coins_500 > 0:
            print(f"500원: {coins_500}개")
        if coins_100 > 0:
            print(f"100원: {coins_100}개")
        if coins_50 > 0:
            print(f"50원: {coins_50}개")
        if coins_10 > 0:
            print(f"10원: {coins_10}개")