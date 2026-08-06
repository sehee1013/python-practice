# 절대값 만드는 함수 정의
def my_abs(n):
    if n < 0:
        return -n
    return n
    
# 정수 n 입력 받기
n = int(input())

# 함수 실행 결과 출력
print(my_abs(n))