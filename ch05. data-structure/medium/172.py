n = int(input())
scores = {}

# n번 입력 받기
for _ in range(n):
    # 학번, 점수 형식으로 입력 받음(쉼표 기준으로 구분)
    student_id, score = map(int, input().split(","))
    # 딕셔너리에 학번, 성적 정보 저장
    scores[student_id] = score

# 조회할 학번 입력 받기
target = int(input())

# 조회한 학번의 성적 출력(없으면 '없음' 출력)
print(scores.get(target, '없음'))