minutes = int(input())
seconds = 0

while True:
    print(f"{minutes}분 {seconds:02}초")
    # 0분 00초 되면 종료 메시지 출력 후 종료
    if minutes == 0 and seconds == 0:
        print("타이머 종료!")
        break
    # 초가 0 되면 분 - 1, 초는 59    
    elif seconds == 0:
        seconds = 59
        minutes -= 1
    else:
        seconds -= 1