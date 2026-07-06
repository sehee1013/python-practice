# N개의 숫자를 입력받아 양수 합, 음수 합, 전체 합을 출력하세요.
n = int(input())

# 각각의 합 변수 선언
pos_sum = 0
neg_sum = 0

# n개 입력 받을 때까지 반복
for _ in range(n):
    # 정수 입력 받기
    num = int(input())
    # 양수, 음수 판별해서 누적합 구하기
    if num > 0:
        pos_sum += num
    elif num < 0:
        neg_sum += num
        
# 결과 출력
print(f"양수 합: {pos_sum}")
print(f"음수 합: {neg_sum}")
print(f"전체 합: {pos_sum + neg_sum}")