total = 0
best = 0

# 조건: 5명의 점수를 받을 때까지 반복
# 동작: 각각의 점수를 total에 더하고, 점수가 best보다 큰 경우 best에 대입
# 평균, 최고점 결과 출력

for i in range(5):
    score = int(input())
    total += score
    if score > best:
        best = score

print(f"평균: {total / 5}")
print(f"최고점: {best}")