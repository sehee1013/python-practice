a_count = 0
b_count = 0
c_count = 0
d_count = 0

# 10명의 점수를 입력 받을 때까지 반복
for _ in range(10):
    # 점수 입력 받기
    score = int(input())
    
    # 90점 이상인 경우
    if score >= 90:
        a_count += 1
    # 80점 이상인 경우
    elif score >= 80:
        b_count += 1
    # 70점 이상인 경우
    elif score >= 70:
        c_count += 1
    # 70점 미만인 경우
    else:
        d_count += 1

# 각 구간 별 인원수 출력
print(f"90점 이상: {a_count}명")
print(f"80점 이상: {b_count}명")
print(f"70점 이상: {c_count}명")
print(f"70점 미만: {d_count}명")