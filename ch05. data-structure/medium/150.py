scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
cutoff = int(input())
pass_names = []
non_pass_names = []

# cutoff 이상이면 합격 list에 추가
pass_names = [name for name, score in scores.items() if score >= cutoff]

# 그렇지 않으면 불합격 list에 추가
non_pass_names = [name for name, score in scores.items() if score < cutoff]

# 각각의 결과 출력
print("합격:", *pass_names)
print("불합격:", *non_pass_names)