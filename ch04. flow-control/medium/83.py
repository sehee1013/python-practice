n = int(input())
total = 0
# 전략:
# 조건: n까지 반복
# 동작: 점수 입력 받고 total에 점수 더함
# 결과: 평균 값 구하고 결과 출력

for student in range(n):
    score = int(input())
    total += score
    
print(f"평균 점수: {total / n}")