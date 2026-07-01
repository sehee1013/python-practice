distance = float(input())
hour = int(input())
total_fee = 0
over_fee = 0
night_fee = 0

# 기본 요금: 4800원
BASIC_FEE = 4800

# 총 요금에 기본 요금 추가하기
total_fee += BASIC_FEE

# 거리 2km 초과하는 경우
if distance > 2:
    # 초과 거리(km단위)당 1000원 추가
    over_fee = int((distance - 2) * 1000)
    total_fee += over_fee

# 22시부터 아침 6시 전 시간에는 야간 할증 20% 추가
if hour >= 22 or hour < 6:
    night_fee = int((total_fee * 0.2))   
    total_fee += night_fee

# 기본요금, 추가요금 출력
print(f"기본요금: {BASIC_FEE}원")
print(f"추가요금: {over_fee}원")

# 야간인 경우만 야간 할증 출력
if night_fee > 0:
    print(f"야간 할증 (20%): {night_fee}원")

# 총 택시비 출력
print(f"총 택시비: {total_fee}원")