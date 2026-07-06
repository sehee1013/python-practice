# 횟수에 따라 등급을 구분하세요
count = int(input())

# 횟수 별 등급 판별
if count >= 60:
    grade = "A"
elif count >= 45:
    grade = "B"
elif count >= 30:
    grade = "C"
elif count >= 15:
    grade = "D"
else:
    grade = "F"

# 결과 출력
print(f"횟수: {count}회 → 등급: {grade}")