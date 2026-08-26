# 정수 x 를 입력에서 읽습니다. 예: "10" → x=10
x = int(input())

# 함수 정의하기
def add_one(n):
    """매개변수 n 을 받아 n = n + 1 후 그 값을 반환"""
    n += 1
    return n
    
# 함수 호출 후 반환값 출력
print(add_one(x))
# 전역변수 x 출력
print(x)