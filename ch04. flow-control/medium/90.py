n = int(input())
count = 0

# 학생 수만큼 반복해서 점수 확인하고 합격자일 경우 합격자 수 증가
for student in range(n):
    score = int(input())
    if score >= 60:
        count += 1

print("합격자 수:", count)