x = int(input())
y = int(input())

# 좌표 tuple 생성 (바뀌지 않기 때문에 tuple 사용)
point = (x, y)

# tuple 언패킹
px, py = point
# x좌표 y좌표 출력
print(f"x: {px}")
print(f"y: {py}")