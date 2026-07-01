pos_sum = 0
neg_sum = 0
zero_count = 0

# 10개 입력 받을 때까지 반복
for _ in range(10):
    # 숫자 입력 받기
    num = int(input())
    # 양수면 양수의 합에 더하기
    if num > 0:
        pos_sum += num
    # 음수면 음수의 합에 더하기
    elif num < 0:
        neg_sum += num
    # 0이면 0의 개수 카운트하기
    else:
        zero_count += 1

# 결과 출력   
print("양수의 합:", pos_sum)
print("음수의 합:", neg_sum)
print("0의 개수:", zero_count)