# 층수를 입력받아 각 층의 요금과 누적 요금을 출력하세요.
n = int(input())

total = 0

# 1층부터 n층까지 반복
for floor in range(1, n + 1):
    charge = floor * 100
    total += charge
    print(f"{floor}층: {charge}원 (누적: {total}원)")