# 미니 인터프리터: SET, ADD, PRINT 명령어를 처리하세요.
n = int(input())
x = 0
y = 0

# n개의 명령어 받을 때까지 반복
for _ in range(n):
    # 명령어 입력 받기
    parts = input().split()
    # 명령어가 SET인 경우, 인덱스[1]가 변수명, 인덱스[2]은 값
    if parts[0] == "SET":
        val = int(parts[2])
        if parts[1] == "x":
            x = val
        elif parts[1] == "y":
            y = val

    # 명령어가 ADD인 경우
    elif parts[0] == "ADD":
        val = int(parts[2])
        if parts[1] == "x":
            x += val
        elif parts[1] == "y":
            y += val
    
    # 명령어가 PRINT인 경우, 인덱스[1]이 변수명
    elif parts[0] == "PRINT":
        if parts[1] == "x":
            print(x)
        elif parts[1] == "y":
            print(y)