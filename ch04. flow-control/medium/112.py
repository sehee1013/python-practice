# 30분 초과분을 10분 단위로 올림 청구

enter_time = int(input())
exit_time = int(input())
parked = exit_time - enter_time

# 기본 요금 30분 이하는 2000원
BASIC_FEE = 2000
BASIC_TIME = 30
# 추가 시간, 추가 요금 변수 선언
over_time = parked - BASIC_TIME
over_fee = 0

# 출력메뉴 상단 출력
print("=== 주차 요금 계산기 ===")
print(f"주차 시간: {parked}분")
print(f"기본 요금: {BASIC_FEE}원")

# 추가 요금: 30분 초과시 10분 당 500원 추가
if (parked) > BASIC_TIME: 

    print(f"추가 시간: {over_time}분")
    over_fee += over_time // 10 * 500

    # 10분 단위가 아닌 경우
    if over_time % 10 != 0:
        over_fee += 500
        
# 추가 요금, 총 요금 출력
print(f"추가 요금: {over_fee}원")
print(f"총 요금: {BASIC_FEE + over_fee}원")