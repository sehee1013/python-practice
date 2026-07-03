max_val = -1

# -1 입력 받기 전까지 계속 반복
while True:
    # 숫자 입력 받기
    num = int(input())
    
    # 입력 받은 숫자가 -1이면 탈출
    if num == -1:
        break
    # 입력 받은 숫자가 max_val보다 크면 max_val에 대입
    elif num > max_val:
        max_val = num

# 입력 받은 숫자가 없으면 경고 메시지 출력
if max_val == -1:
    print("입력한 숫자가 없습니다.")
# 그 외, 결과 출력
else:
    print(f"최대값: {max_val}")
