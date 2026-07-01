age = int(input())
group_count = int(input())

# 전략:
# 1. 나이, 인원 순으로 판별
# 2. 나이 구간 별 요금 배정
# 3. 인원 수 10명 이상일 경우 전체 금액에서 20% 할인

# 나이 판별 후 입장료 책정
if age <= 3:
    price = 0
elif age <= 12:
    price = 15000
elif age <= 18:
    price = 20000
elif age <= 64:
    price = 30000
else:
    price = 10000

print(f"기본 입장료: {price}원")

# 인원 수 10명 이상인 경우, 단체 할인 안내 메시지 출력 후 할인된 가격 출력
if group_count >= 10:
    price = int(price * 0.8)
    print("단체 할인 적용 (20%)!")
    print(f"1인 할인가: {price}원")

print(f"총 입장료: {price * group_count}원")