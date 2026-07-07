# 금액을 입력받아 최소 동전 수로 거슬러 주세요.
money = int(input())

total_count = 0

for coin in (500, 100, 50, 10):
    # coin원 개수: money // coin
    coin_count = money // coin

    # 동전 별 개수 출력
    print(f"{coin}원: {coin_count}개")

    # 총 동전 수에 더하기
    total_count += coin_count

    # 이후 금액: money % coin
    money %= coin

# 결과 출력
print(f"총 동전 수: {total_count}개")