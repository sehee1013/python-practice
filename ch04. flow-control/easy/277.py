# 바깥 if는 배차 가능 여부, 안쪽 if는 목적지 유무로 작성하세요.
available = input() == "True"
destination = input()

# 배차 가능한 경우 목적지 확인:
if available:

    # 목적지가 입력된 경우 운행 시작 출력
    if destination:
        print("운행 시작")

    # 목적지가 없는 경우 목적지 입력하라는 문구 출력
    else:
        print("목적지를 입력하세요")

# 배차가 없는 경우 차량 대기 문구 출력
else:
    print("차량 대기 중")