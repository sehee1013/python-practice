# 조건 표현식을 컴프리헨션 표현식 자리에 둡니다.
data_sets = [
    [-3, 5, -1, 0, 4, -7, 2, -10, 8],
    [-1, -5, -10],
    [10, 20, 30],
]
t = int(input())
data = data_sets[t]

# 음수는 0으로, 양수와 0은 그대로 두기
result = [max(num, 0) for num in data]

# 결과 출력
print(*result)