goal = int(input())
saved = 0

# 저축액이 목표액보다 작으면 계속 반복
while saved < goal:
    # 현재 금액과 목표 금액 출력
    print(f"현재: {saved}원 / 목표: {goal}원")
    
    # 동전 금액 하나씩 입력 받기
    money_value = int(input())
    
    # 입력 받은 값 saved에 더하기
    saved += money_value

# 현재 금액과 목표 금액 한 번 더 출력
print(f"현재: {saved}원 / 목표: {goal}원")

# 목표 달성 시 총 저축액 출력
print(f"목표 달성! 총 {saved}원을 모았습니다.")