principal = int(input())
annual_rate = int(input())
target_amount = int(input())
year = 0

while True:
    # 자산 갱신 계산
    principal = principal + (principal * annual_rate) // 100
    
    year += 1

    # 자산 목표 이상 되면 종료
    if principal >= target_amount:
        print(f"{year}년 차에 목표 도달 (자산: {principal}만원)")
        break
    # 50년 지나도 도달 못하면 종료
    elif year == 50:
        print("50년 안에 도달 불가")
        break