names  = ["윤서", "지우", "민준", "서윤", "도윤"]
scores = [85, 92, 65, 78, 95]
n = int(input())

# n등 학생의 이름과 점수 출력
# 점수와 이름 튜플로 묶어 리스트 변환
scores_names = [(score, name) for score, name in zip(scores, names)]

# 점수 순으로 정렬 후 출력
scores_names.sort(reverse=True)
rank_score, rank_name = scores_names[n - 1]

print(f"{rank_name}: {rank_score}")