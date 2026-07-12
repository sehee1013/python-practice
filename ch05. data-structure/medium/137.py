data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# max와 min 구하기
max_num = max(scores)
min_num = min(scores)

# scores의 각 점수들 순회하며 정규화. 계산 결과값 소수점 둘째 자리까지 구하기
result = [f"{(score - min_num) / (max_num - min_num):.2f}" for score in scores]

# result 공백 구분하여 출력
print(" ".join(map(str, result)))