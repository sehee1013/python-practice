# "예"로 답한 재료만 이어 붙여 "나의 파스타: ..." 형식으로 출력하세요.
add_cheese = input()
add_bacon = input()
add_shrimp = input()
pasta = "파스타"

# 치즈 추가하는 경우 pasta에 " + 치즈" 더하기
if add_cheese == "예":
    pasta += " + 치즈"
# 베이컨 추가하는 경우 pasta에 " + 베이컨" 더하기
if add_bacon == "예":
    pasta += " + 베이컨"
# 새우 추가하는 경우 pasta에 " + 새우" 더하기
if add_shrimp == "예":
    pasta += " + 새우"

# 최종 파스타 출력 "나의 파스타: "
print(f"나의 파스타: {pasta}")