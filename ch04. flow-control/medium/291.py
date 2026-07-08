# 등급별 카운터 5개를 두고 N번 반복하며 입력 점수에 맞는 카운터를 증가시키세요.
n = int(input())
# TODO
parts = [" 0~59", "60~69", "70~79", "80~89", "90~100"]

# 각 구간 별 학생 수
counts = [0] * 5

# n명의 점수를 받을 때까지 반복
for _ in range(n):
    # 점수 입력 받기
    score = int(input())

    score_digit_10 = score // 10

    # 점수 구간 판별
    if score_digit_10 < 6:
        idx = 0
    elif score_digit_10 == 6:
        idx = 1
    elif score_digit_10 == 7:
        idx = 2
    elif score_digit_10 == 8:
        idx = 3
    else:
        idx = 4
    
    # 카운트 + 1
    counts[idx] += 1

# 결과 출력
print(f"A ({parts[4]}): {counts[4]}명")
print(f"B ({parts[3]}): {counts[3]}명")
print(f"C ({parts[2]}): {counts[2]}명")
print(f"D ({parts[1]}): {counts[1]}명")
print(f"F ({parts[0]}): {counts[0]}명")