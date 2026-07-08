# N명의 목적지를 입력받아 엘리베이터 운행을 시뮬레이션하세요.
n = int(input())

# 층 각각의 변수 선언
floor1 = 0
floor2 = 0
floor3 = 0
floor4 = 0
floor5 = 0
floor6 = 0
floor7 = 0
floor8 = 0
floor9 = 0
floor10 = 0

max_floor = 0

# n명의 목적지 층 입력 받기
for _ in range(n):
    target_floor = int(input())

    # 목적지 층 별로 카운트    
    if target_floor == 2:
        floor2 += 1
        if max_floor < 2:
            max_floor = 2
    
    elif target_floor == 3:
        floor3 += 1
        if max_floor < 3:
            max_floor = 3
    
    elif target_floor == 4:
        floor4 += 1
        if max_floor < 4:
            max_floor = 4
    
    elif target_floor == 5:
        floor5 += 1
        if max_floor < 5:
            max_floor = 5
    
    elif target_floor == 6:
        floor6 += 1
        if max_floor < 6:
            max_floor = 6
    
    elif target_floor == 7:
        floor7 += 1
        if max_floor < 7:
            max_floor = 7
    
    elif target_floor == 8:
        floor8 += 1
        if max_floor < 8:
            max_floor = 8
    
    elif target_floor == 9:
        floor9 += 1
        if max_floor < 9:
            max_floor = 9
    
    elif target_floor == 10:
        floor10 += 1
        max_floor = 10

# 목적지 층의 카운트가 0 보다 크면 출력
if floor2 > 0:
    print(f"2층: {floor2}명 하차")
if floor3 > 0:
    print(f"3층: {floor3}명 하차")
if floor4 > 0:
    print(f"4층: {floor4}명 하차")
if floor5 > 0:
    print(f"5층: {floor5}명 하차")
if floor6 > 0:
    print(f"6층: {floor6}명 하차")
if floor7 > 0:
    print(f"7층: {floor7}명 하차")
if floor8 > 0:
    print(f"8층: {floor8}명 하차")
if floor9 > 0:
    print(f"9층: {floor9}명 하차")
if floor10 > 0:
    print(f"10층: {floor10}명 하차")


# 결과 출력
print(f"운행 완료 (최고층: {max_floor}층)")