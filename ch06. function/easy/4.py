# 직사각형의 가로, 세로 길이(정수형)을 입력받아 넓이 반환
def area(w, h):
    return w * h

# input().split() 으로 두 칸을 나눠 각각 정수로 바꿉니다. 예: "4 5" → w=4, h=5
w, h = [int(x) for x in input().split()]

# 넓이 함수 반환값 출력
print(area(w, h))