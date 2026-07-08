n = int(input())
total = 0

# 점수 n번 입력 받을 때까지 반복
for _ in range(n):
    # 점수 입력 받기
    score = int(input())

    # 0 미만, 100 초과 점수인 경우 무효 출력 후 건너뛰기
    if not(0 <= score <= 100):
        print("무효:", score)
        continue

    # 유효하면 합계 누적
    total += score

# 결과 출력
print("유효 점수의 합:", total)