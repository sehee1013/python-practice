# 사이즈별 단가를 정하고, 3판 이상이면 10% 할인
size = input().strip().upper()
qty = int(input())

# 할인 플래그
is_discount = False

# 사이즈별 가격 딕셔너리 생성
pizza_price = {
    "S": 8000,
    "M": 12000,
    "L": 15000
}

# 주문액 계산
total_price = pizza_price[size] * qty

# 3판 이상 주문시 할인 10%
if qty >= 3:
    total_price *= 0.9
    is_discount = True

# 결과 출력
print(f"사이즈: {size} | 수량: {qty}판")
print(f"총액: {round(total_price)}원")

# 할인받은 경우에만 출력
if is_discount:
    print("(10% 할인 적용)")