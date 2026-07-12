names  = ["윤서", "지우", "민준", "서윤", "도윤"]
scores = [85, 92, 65, 78, 95]
n = int(input())

# 점수가 n 이상인 학생 이름 입력 순서대로 출력
# 모든 학생과 점수 순회, n 이상이면 리스트 추가
pass_std = [name for name, score in zip(names, scores) if score >= n]

# 결과 출력
print(" ".join(pass_std))