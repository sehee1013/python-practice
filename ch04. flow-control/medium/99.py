mode = int(input())
n = int(input())
unit = ""
max_temp = -9999
min_temp = 9999


# 온도 n개 입력을 때까지 반복
for _ in range(n):
    # 온도 입력 받기
    temp = int(input())
    # 모드 1인 경우
    if mode == 1:
        temp = temp * 9 / 5 + 32
        unit = "°F"
    elif mode == 2:
        temp = (temp - 32) * 5 / 9
        unit = "°C"

    # 변환 결과 출력
    print(f"변환 결과: {temp}{unit}")

    # 온도가 max_temp보다 높으면 대입
    if temp > max_temp:
        max_temp = temp
    # 온도가 min_temp보다 낮으면 대입
    if temp < min_temp:
        min_temp = temp

# 최고, 최저 변환 온도 출력
print("최고 변환 온도:", max_temp)
print("최저 변환 온도:", min_temp)