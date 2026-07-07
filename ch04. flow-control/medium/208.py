n = int(input())
total = 0

# 가격 n개 입력 받을 때까지 반복
for _ in range(n):
    # 가격 입력 받기
    price = int(input())

    # 가격이 10000원 이상인 경우만 20% 할인 적용
    if price >= 10000:
        price = (price * 4) // 5

    # 가격 total에 더함
    total += price

# 총액 출력
print(f"총액: {total}원")