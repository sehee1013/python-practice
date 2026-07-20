# 각 줄을 `split(",")` 후 int 로 변환, 소계 누적.
n = int(input())
total_price = 0

# n번 이름, 수량, 단가 형식으로 입력 받아 ","기준으로 구분
for _ in range(n):
    item, count_str, price_str = input().split(',')
    
    # 정수형으로 형 변환
    count, price = int(count_str), int(price_str) 
    # 상품 총액 구하기
    subtotal = price * count
    
    # 누적 총액에 상품 총액 더하기
    total_price += subtotal

    # 이름, 수량, 각 상품의 총 가격 출력
    print(f"{item} x{count}: {subtotal}원")

# 누적 총액 출력
print(f"총액: {total_price}원")