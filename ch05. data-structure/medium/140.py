data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 0부터 마지막까지 반복하여 평균 구하고 리스트에 추가
result = [sum(scores[:i + 1]) / len(scores[:i + 1]) for i in range(len(scores))]

# 소숫점 한자리까지 결과 출력
print(" ".join(f'{average:.1f}' for average in result))