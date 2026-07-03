temp = float(input())

# 온도 5도 미만: 패딩, 두꺼운 목도리
if temp < 5:
    recommend_dress = "패딩, 두꺼운 목도리"    
# 온도 5도 이상 10도 미만: 코트, 니트
elif temp < 10:
    recommend_dress = "코트, 니트"
# 온도 10도 이상 20도 미만: 자켓, 가디건
elif temp < 20:
    recommend_dress = "자켓, 가디건"
# 온도 20도 이상 28도 미만: 반팔, 얇은 셔츠
elif temp < 28:
    recommend_dress = "반팔, 얇은 셔츠"
# 온도 28도 이상: 민소매 반바지
else:
    recommend_dress = "민소매, 반바지"

# 현재 기온, 추천 옷차림 출력
print(f"현재 기온: {temp}°C")
print(f"추천 옷차림: {recommend_dress}")