# float로 입력받아 구간별로 판정하세요.
distance = float(input())
transport = ""

# 2km 미만 도보
if distance < 2:
    transport = "도보"
# 2km 이상 5km 미만 자전거
elif distance < 5:
    transport = "자전거"
# 5km 이상 20km미만 버스
elif distance < 20:
    transport = "버스"
# 20km 이상 지하철
else:
    transport = "지하철"

# 입력 거리와 추천 교통수단 출력
print(f"거리: {distance}km\n추천 교통수단: {transport}")