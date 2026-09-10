# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "4 5" → w=4, h=5
w, h = [int(x) for x in input().split()]

# 함수 정의하기
def rect(w, h):
    """둘레와 넓이를 반환하기"""
    return (w + h) * 2, w * h

# 함수 호출 후 언패킹
perimeter, area = rect(w, h)

# 결과 출력
print(perimeter, area)