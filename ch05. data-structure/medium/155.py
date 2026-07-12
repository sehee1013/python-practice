scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
target = int(input())

# 역방향 딕셔너리 생성
reversed_scores = {score:name for name, score in scores.items()}

# 해당 점수의 학생 출력
if target in reversed_scores:
    print(reversed_scores[target])
else:
    print("없음")