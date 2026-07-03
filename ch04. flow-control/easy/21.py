amount = int(input())

# 500원부터 100원, 50원, 10원 각 동전의 최소 개수 구함.
coin_500 = amount // 500
change = amount % 500

coin_100 = change // 100
change %= 100

coin_50 = change // 50
change %= 50

coin_10 = change // 10

# 총 동전 수 구하기
total_coin_num = coin_500 + coin_100 + coin_50 + coin_10
#각 동전 수, 총 동전 수 출력
print(f"{amount}원 → 동전 변환:")
print(f"500원: {coin_500}개")
print(f"100원: {coin_100}개")
print(f"50원: {coin_50}개")
print(f"10원: {coin_10}개")
print(f"총 동전 수: {total_coin_num}개")