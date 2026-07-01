positive = 0
negative = 0
zero = 0
# 조건: 10개의 정수를 입력 받을 때까지 반복
# 동작: 입력 받은 정수가 음수인지 정수인지 0인지 판별 후 카운트
# 결과: 판별 결과 출력

for _ in range(10):
    num = int(input())
    if num < 0:
        negative += 1
    elif num == 0:
        zero += 1
    else:
        positive += 1

print(f"양수: {positive}개")
print(f"음수: {negative}개")
print(f"0: {zero}개")