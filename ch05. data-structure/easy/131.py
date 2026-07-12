# 최댓값 위치를 찾아 이름 리스트에서 같은 인덱스 학생 출력.
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

max_name, max_score = names[0], scores[0]

# 이름과 점수 묶어서 가장 큰 점수의 학생 이름 넣기
for name, score in zip(names[1:], scores[1:]):
    if score > max_score:
        max_name, max_score = name, score
        
# 결과 출력
print(max_name)