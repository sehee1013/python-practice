# 7일 초과분에 대해 일당 200원 부과
days = int(input())

# 대여일 <= 7인 경우 무료
if days <= 7:
    rental_fee = 0
# 그 외는 일당 200원씩 추가
else:
    rental_fee = 200 * (days - 7)

# 결과 출력
print(f"대여 일수: {days}일")
print(f"대여료: {rental_fee}원")