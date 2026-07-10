# 슬라이싱 `lst[:N]` 으로 처음 N개를 한 번에 추출할 수 있습니다.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
n = int(input())

# 슬라이싱으로 처음 N개만 추출 후 출력
front_scores = scores[:n]

# 결과 출력. 사이에 공백 추가
print(" ".join(map(str, front_scores)))