# 언패킹은 `좌변의 변수 개수`와 `tuple 원소 개수`가 같아야 합니다.
r = int(input())
g = int(input())
b = int(input())

# color tuple 생성
color = (r, g, b)

# tuple 언패킹
r, g, b = color

# 결과 출력
print(f"R: {r}")
print(f"G: {g}")
print(f"B: {b}")