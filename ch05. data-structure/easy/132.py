# min 위치를 찾아 이름 출력.
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

# 점수 리스트의 최저점 value의 인덱스 반환
index = scores.index(min(scores))

# 이름 리스트에 추출 인덱스로 접근 후 출력
print(names[index])