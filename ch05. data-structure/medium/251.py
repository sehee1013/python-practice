# 정수 리스트로 변환 후 sorted 의 결과를 [1:-1] 로 잘라내 평균을 따로 구하세요.
n = int(input())

# 점수 리스트 입력 받기
scores = list(map(int, input().split()))

# 원본 점수 리스트 평균을 구하기
original_avg = sum(scores) / n

# 점수 정렬하기
sorted_scores = sorted(scores)
# 최고점, 최저점 제거하기
filtered_scores = sorted_scores[1:-1]

# 보정된 점수 리스트 평균 구하기
filtered_avg = sum(filtered_scores) / len(filtered_scores)

# 원본 평균, 보정 평균 출력
print(f"원본 평균: {original_avg:.1f}")
print(f"보정 평균: {filtered_avg:.1f}")