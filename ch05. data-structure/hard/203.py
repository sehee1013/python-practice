# scores 를 순회하면서 `s <= q` 인 개수를 세고, 비율을 백분율로 변환.
scores = [85, 92, 65, 78, 95, 70, 88, 72, 90, 100]
q = int(input())

# q 이하인 점수의 개수 구하기
lower_than_q = [score for score in scores if q >= score]
# 백분위 구하기
percentile = (len(lower_than_q) / len(scores)) * 100

# 결과 출력
print(f"백분위: {percentile:.1f}")