# 흙 상태로 먼저 분기하고, 그 안에서 햇빛 세기를 검사하세요.
soil_dry = input() == "True"
strong_sun = input() == "True"

# 흙이 말랐는 경우
if soil_dry:
    # 햇빛이 강한 경우
    if strong_sun:
        print("물 듬뿍")
    # 햇빛이 강하지 않은 경우
    else:
        print("물 조금")
# 흙이 마르지 않은 경우
else:
    print("물 안 줘도 돼요")