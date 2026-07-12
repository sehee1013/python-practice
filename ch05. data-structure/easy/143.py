scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())

# 딕셔너리 순회하며 성적 판별, cutoff 이상인 경우 리스트 추가
result = [name for name, score in scores.items() if score >= cutoff]

# 결과 출력
print(" ".join(result))