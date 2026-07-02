# 합이 target인 두 수의 쌍을 출력하세요.
N = int(input())
target = int(input())

# 1부터 N까지 반복
for first in range(1, N + 1):

    second = target - first
    
    # target - num < N 인 경우
    if second <= N and first < second:            

        # num과 target - num 출력
        print(f"({first}, {second})")