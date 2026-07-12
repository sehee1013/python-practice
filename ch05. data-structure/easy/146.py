scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 평균 구하기
average = sum(scores.values()) / len(scores)

# 점수 - 평균의 절대값 구하기
gap = abs(scores[name] - average)

# 소수점 첫째 자리까지 출력
print(f"차이: {gap:.1f}")