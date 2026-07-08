# N과목의 학점과 이수학점을 입력받아 GPA를 계산하세요.
n = int(input())
total_credits = 0
weighted_sum = 0

# 학점과 이수학점을 n번 입력 받기
for subject in range(1, n + 1):
    # 공백으로 구분하여 각각 학점, 이수학점으로 다룸
    parts = input().split()

    grade = parts[0]
    credit = int(parts[1])

    # 과목, 학점, 이수학점 출력
    print(f"과목{subject}: {grade} ({credit}학점)")

    # 총 이수학점 구하기
    total_credits += credit

    # 취득한 학점 별 점수 변환
    if grade == "A+":
        score = 4.5
    elif grade == "A":
        score = 4.0
    elif grade == "B+":
        score = 3.5
    elif grade == "B":
        score = 3.0
    elif grade == "C+":
        score = 2.5
    elif grade == "C":
        score = 2.0
    elif grade == "D+":
        score = 1.5
    elif grade == "D":
        score = 1.0
    elif grade == "F":
        score = 0.0

    weighted_sum += score * credit

# GPA 계산하기
gpa = weighted_sum / total_credits

# 결과 출력
print(f"GPA: {gpa:.2f}")