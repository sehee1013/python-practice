n = int(input())

# 학생 점수 n번 입력 받을 때까지 반복
for turn in range(1, n + 1):
    # 점수 입력 받기
    score = int(input())
    # 점수에 따라 별 개수 출력
    if score >= 90:
        print(f"{turn}번 학생: ★★★★★")
    elif score >= 80:
        print(f"{turn}번 학생: ★★★★")
    elif score >= 70:
        print(f"{turn}번 학생: ★★★")
    elif score >= 60:
        print(f"{turn}번 학생: ★★")
    else:
        print(f"{turn}번 학생: ★")