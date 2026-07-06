# 반복문으로 각 음료 가격을 입력받아 포인트를 누적하세요
n = int(input())
point= 0

# n만큼 반복하여 음료 가격 입력 받기
for _ in range(n):
    # 음료 가격 입력
    price = int(input())

    # 적립 포인트 계산 후 누적
    point += price // 20

# 스탬프는 n // 3
stamp = n // 3

# 결과 출력
print(f"총 구매: {n}잔")
print(f"총 적립 포인트: {point}점")
print(f"스탬프: {stamp}개")