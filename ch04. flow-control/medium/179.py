# 22시 이후 시간을 구분하여 야간수당을 계산하세요
wage = int(input())
hours = int(input())
start = int(input())
week_holiday_pay = 0

# 야간 수당 계산하기
night_hours = max(0, (hours + start) - 22)
day_hours = hours - night_hours

# 기본 급여
basic_pay = (day_hours + night_hours * 1.5) * wage
# 주휴 수당: 기본 급여의 20%
week_holiday_pay = int(basic_pay * 0.2)
total_pay = int(week_holiday_pay + basic_pay)

# 결과 출력
print(f"시급: {wage}원 | 근무: {hours}시간 ({start}시 시작)")
print(f"기본급: {int(basic_pay)}원")
print(f"주휴수당: {week_holiday_pay}원")
print(f"총 급여: {total_pay}원")