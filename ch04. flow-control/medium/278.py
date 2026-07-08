is_member = input() == "True"
hours = int(input())
BASIC_FEE = 2000

# 회원인 경우 
if is_member:
    # 1시간 이하인 경우
    if hours <= 1:
        print("무료")
    # 1시간 초과인 경우
    else:
        print(f"요금: {(hours - 1) * 1000}원")
# 회원이 아닌 경우
else:
    # 1시간 이하인 경우
    if hours <= 1:
        print(f"요금: {BASIC_FEE}원")
    # 1시간 초과인 경우
    else:
        print(f"요금: {BASIC_FEE + (hours - 1) * 2000}원")       