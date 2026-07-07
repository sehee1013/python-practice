# 구간별 개수를 세고, 0이 아닌 구간만 출력하세요.
n = int(input())

# 각 구간 별 학생 수 
count_over_90 = 0
count_80s = 0
count_70s = 0
count_60s = 0
count_50s = 0
count_40s = 0
count_30s = 0
count_20s = 0
count_10s = 0
count_lower_10 = 0

# n명의 점수 입력 받을 때까지 반복
for _ in range(n):
    # 점수 입력 받기
    score = int(input())    
    # 점수 구간 판별
    if score > 100 or score < 0:
        print("잘못된 점수입니다.")
    elif score >= 90:
        count_over_90 += 1
    elif score >= 80:
        count_80s += 1
    elif score >= 70:
        count_70s += 1
    elif score >= 60:
        count_60s += 1
    elif score >= 50:
        count_50s += 1
    elif score >= 40:
        count_40s += 1
    elif score >= 30:
        count_30s += 1
    elif score >= 20:
        count_20s += 1
    elif score >= 10:
        count_10s += 1
    else:
        count_lower_10 += 1

    
# 결과 출력
if count_lower_10 > 0:
    print(f"0~9: {'#' * count_lower_10}")
if count_10s > 0:
    print(f"10~19: {'#' * count_10s}")
if count_20s > 0:
    print(f"20~29: {'#' * count_20s}")
if count_30s > 0:
    print(f"30~39: {'#' * count_30s}")
if count_40s > 0:
    print(f"40~49: {'#' * count_40s}")
if count_50s > 0:
    print(f"50~59: {'#' * count_50s}")
if count_60s > 0:
    print(f"60~69: {'#' * count_60s}")
if count_70s > 0:
    print(f"70~79: {'#' * count_70s}")
if count_80s > 0:
    print(f"80~89: {'#' * count_80s}")
if count_over_90 > 0:
    print(f"90~100: {'#' * count_over_90}")