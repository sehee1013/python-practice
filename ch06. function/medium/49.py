# 전역 x=첫 값, a=둘째, b=셋째. 예: "10 20 30" → x=10, a=20, b=30
parts = input().split()
x = int(parts[0])
a = int(parts[1])
b = int(parts[2])

# global 선언하지 않는 함수 정의하기
def without_global(v):
    """지역변수 x에만 v를 대입. 전역 x는 변경되지 않음"""
    x = v

# global 선언하는 함수 정의하기
def with_global(v):
    """전역변수 x에만 v를 대입. 전역 x는 변경됨"""    
    global x
    x = v

# 각각의 함수 호출하여 실행하고 전역변수 x 출력
without_global(a)
print(x)
with_global(b)
print(x)