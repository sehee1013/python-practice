# 전략: 처음 입력 받은 값을 minimum으로 두고 나머지와 대소 관계 비교
# 조건: 4개 받을 때까지 반복
# 동작: 입력 받은 정수가 minimum보다 작으면 num을 minimum에 대입
# 결과: minimum 출력
minimum = int(input())

for _ in range(4):
    num = int(input())
    if num < minimum:
        minimum = num
        
print(f"최소값: {minimum}")