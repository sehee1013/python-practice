# 1부터 n까지의 합을 구하는 함수 정의
def sum_to(n):
    total_sum = 0
    for i in range(1, n + 1):
       total_sum += i
    return total_sum           

# 정수 n 입력 받기
n = int(input())

# 함수 실행 결과 출력
print(sum_to(n))