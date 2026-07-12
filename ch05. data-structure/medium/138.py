names_sets = [
    ["윤서", "지우", "민준", "서윤", "도윤"],
    ["A", "B", "C"],
    ["X", "Y"],
]
scores_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
names = names_sets[t]
scores = scores_sets[t]

# 평균 계산하기
average = sum(scores) / len(scores)

# 변수 초기 설정
best_diff = abs(average - scores[0])
best_idx = 0

# 인덱스와 성적 가져와서 절대값이 평균과 가장 가까운 것 선택(평균 - 성적)
for idx, score in enumerate(scores):

    # 절대값 구하기
    diff = abs(average - score)

    # 기존의 최소 절대값보다 절대값이 더 작은 경우 갱신
    if diff < best_diff:
        best_diff = diff
        best_idx = idx

# 결과 출력
print(f"{names[best_idx]}: {scores[best_idx]}")