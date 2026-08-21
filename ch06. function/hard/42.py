# 전역 count = 첫 값, step = 둘째 값. 예: "100 5" → count=100, step=5
parts = input().split()
count = int(parts[0])
step = int(parts[1])

# 함수 정의하기
def bump():
    """지역변수 count를 step으로 두고 그 값 반환하기"""
    count = step
    return count

# 함수 호출하여 실행한 첫번째 결과 출력하기
print(bump())
# 함수 호출하여 실행한 두번째 결과 출력하기
print(bump())
# 전역변수 count 출력하기
print(count)