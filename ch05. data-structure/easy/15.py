# 합과 개수로 평균을 구하고 소수점 첫째 자리 포맷으로 출력하세요.
data_sets = [
    [85, 92, 78, 95, 88, 70, 100, 65, 82, 90],
    [50, 60, 70],
    [100],
]
t = int(input())
scores = data_sets[t]

# sum()로 모든 점수의 합 구해서 변수에 대입
total = sum(scores)

# len()로 리스트 길이 구하고 평균 계산
average = total / len(scores)

# 결과 출력. 평균은 소숫점 1의 자리까지만 출력
print(f"총합: {total}")
print(f"평균: {average:.1f}")