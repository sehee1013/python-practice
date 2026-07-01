score = int(input())
attendance = int(input())
# 전략:
# 1. 등급, 수료 여부 순으로 판단
# 2. 점수 구간 별 등급 부여
# 3. 등급이 F이거나 출석률이 80 미만이면 미수료

# 점수 구간 별 등급 부여
if score < 60:
    score_grade = "F"
elif score <70:
    score_grade = "D"
elif score <80:
    score_grade = "C"
elif score <90:
    score_grade = "B"
else:
    score_grade = "A"

# 등급 판별 결과 출력
print(f"등급: {score_grade}")

# F인 경우, 출석률 판단 없이 바로 결과 출력
if score_grade == "F":
    print("미수료 - 성적 미달 (60점 이상 필요)")
elif attendance < 80:
    print("미수료 - 출석률 부족 (80% 이상 필요)")
else:
    print("수료를 축하합니다!")