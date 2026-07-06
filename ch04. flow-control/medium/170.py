# 교시별 과목 배정 후 표 형태로 출력하세요.
n = int(input())

# 시간표 딕셔너리 생성
time_table = {
    1: "-",
    2: "-",
    3: "-",
    4: "-",
    5: "-",
    6: "-"
}

# n번 입력 받을 때까지 반복
for _ in range(n):
    # 과목 정보 입력 받기
    sub_info = input()
    # 공백 기준으로 나누기
    sub_info_list = sub_info.split()

    # idx = 0 은 sub, idx = 1 은 start, idx = 2는 end
    sub = sub_info_list[0]
    start = int(sub_info_list[1])
    end = int(sub_info_list[2])
    
    # 딕셔너리에 저장
    for time in range(start, end + 1):

        # 해당 교시에 이미 다른 과목이 있으면 건너뜀
        if time_table[time] != "-":
            continue

        time_table[time] = sub

# 카테고리 출력
print("교시 | 과목")
print("-----|------")

# 1교시부터 6교시까지 출력
for time in time_table:
    print(f"{time}교시 | {time_table[time]}")