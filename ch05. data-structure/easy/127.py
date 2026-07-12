# 합 / 개수로 평균 산출, `:.1f` 포맷.
data_sets = [
    [85, 92, 65, 78, 95],
    [80, 90, 70],
    [50, 60],
]
t = int(input())
scores = data_sets[t]

# 합과 개수 구해서 평균 구하기
average = sum(scores) / len(scores)

# 소숫점 1의 자리까지 출력
print(f"평균: {average:.1f}")