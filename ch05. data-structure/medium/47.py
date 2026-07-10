# 평균은 컴프리헨션 바깥에서 미리 계산해 두고, 컴프리헨션 안에서는 `x - mean` 만 표현하세요.
# 정수 나눗셈 `//` 을 사용해야 결과가 정수가 됩니다.
data = [10, 20, 30, 40, 50]
n = int(input())

# 평균 구하기
average = sum(data[:n]) // n

sub = data[:n]

# 리스트 값 순회하면서 평균 빼기
result = [num - average for num in sub]

# 출력
print(*result)