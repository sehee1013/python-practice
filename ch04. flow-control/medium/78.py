currency = int(input())
krw = int(input())
EXCHANGE_FEE = 0.015

# 전략:
# 1. 환율 딕셔너리 생성
# 2. 딕셔너리에 없는 값 입력되면 경고 메시지 출력
# 3. 입력된 원화 금액 환전 후 결과 출력

exchange_dict = {
    1 : {"currencies":"달러", "rates":1350}, 
    2 : {"currencies":"엔", "rates":9},
    3 : {"currencies":"유로", "rates":1450} 
}

# 1, 2, 3이 아닐 경우 경고 메시지 출력
if currency in exchange_dict:
    exchange_money = round(krw / exchange_dict[currency]['rates'], 2)
    print(f"환전 금액: {exchange_money} {exchange_dict[currency]['currencies']}")
    print(f"수수료 (1.5%): {int(krw * EXCHANGE_FEE)}원")
    print(f"실 지불 금액: {int(krw + krw * EXCHANGE_FEE)}원")

else:
    print("잘못된 통화 선택입니다.")