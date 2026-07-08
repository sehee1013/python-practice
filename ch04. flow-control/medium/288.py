count_a = 0
count_b = 0
count_c = 0
count_f = 0

# 0 입력 전까지 반복
while True:
    # 점수 입력 받기
    score = int(input())

    # 탈출 조건 생성
    if score == 0:
        break
    # 점수 구간 별 등급 판별 후 카운트
    elif score  < 0:
        print("잘못된 점수")
    elif score > 100:
        print("점수 초과")
    elif score >= 90:
        count_a += 1
    elif score >= 80:
        count_b += 1
    elif score >= 70:
        count_c += 1
    else:
        count_f += 1

# 결과 출력
print(f"A: {count_a} B: {count_b} C: {count_c} F: {count_f}")