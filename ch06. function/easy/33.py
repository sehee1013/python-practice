# 함수 정의하기
def paint():
    """color=inner로 두고 color 반환"""
    color = inner
    return color

parts = input().split()
color = parts[0]
inner = parts[1]

# 함수 호출하여 실행 결과 출력
print(paint())
# 전역 변수 color 출력
print(color)