order_type = input().strip()
price = 15000

order_types = ["배달", "포장"]
# 상수 설정
DELIVERY_BASE_DISTANCE = 3

# 주문 처리: 주문 방식 -> 거리 순으로 확인
# 배달이면 거리 3키로 이하: 배달비 2000원 3키로 초과: 배달비 3500
if order_type in order_types:
    if order_type == "배달":
        delivery_distance = int(input())
        if delivery_distance <= DELIVERY_BASE_DISTANCE:
            delivery_fee = 2000
        else:
            delivery_fee = 3500
        total_price = price + delivery_fee
        # 주문 방식, 배달비, 총 결제 금액 출력
        print(f"배달 주문: 음식 {price}원 + 배달비 {delivery_fee}원 = 총 {total_price}원")
    # 포장은 2000원 할인
    else:
        # 주문 방식, 할인 금액, 총 결제 금액 출력
        print(f"포장 주문: 음식 {price}원 - 할인 2000원 = 총 {price - 2000}원")
# 그 외는 잘못된 주문 방식
else:
    print("잘못된 주문 방식입니다.")