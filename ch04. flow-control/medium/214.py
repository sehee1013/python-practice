shape = input().strip()

# 도형 종류에 따라 면적 구하기
# 원인 경우, 반지름 입력 받기
if shape == "원":
    radius = int(input())

    area = round((radius ** 2 * 3.14), 2)
    print(f"넓이: {area:.2f}")
# 삼각형인 경우, 밑변과 높이 입력 받기
elif shape == "삼각형":
    length = int(input())
    height = int(input())

    area = (length * height) / 2
    # 결과 출력
    print(f"넓이: {area:.1f}")
# 사각형인 경우, 가로와 세로 길이 입력 받기
elif shape == "사각형":
    horizon = int(input())
    vertical = int(input())

    area = horizon * vertical
    # 결과 출력
    print(f"넓이: {area}")
else:
    print("잘못된 입력입니다.")
    exit()