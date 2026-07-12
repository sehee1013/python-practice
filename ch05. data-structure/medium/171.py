n = int(input())
total_score = 0

# n번 입력 받기 반복
for _ in range(n):
    # 이름, 점수 형식으로 입력 받아 쉼표 기준으로 구분
    name, score = input().split(",")
    # 점수 정수형으로 변환하여 누적합 구하기
    total_score += int(score)
    
# 평균 구하기
average = total_score / n
# 소숫점 1번째까지 결과 출력
print(f"평균: {average:.1f}")