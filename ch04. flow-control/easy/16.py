month = int(input())
season = ""

# 1~12를 입력한 경우
if 1 <= month <= 12:
    # 3,4,5인 경우 "봄" 
    if 3 <= month <= 5: 
        season = "봄"
    # 6,7,8인 경우 "여름" 
    elif 6 <= month <= 8:
        season = "여름"
    # 9,10,11인 경우 "가을" 
    elif 9 <= month <= 11:
        season = "가을"
    # 12,1,2인 경우 "겨울"
    else:
        season = "겨울" 

    # 월, 계절 출력
    print(f"{month}월은 {season}입니다.")