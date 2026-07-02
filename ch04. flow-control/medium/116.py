# 각 학생 점수 입력 후 target 점수를 고르고 더 높은 수 세기
print("=== 5명의 점수 입력 ===")
s1 = int(input())
s2 = int(input())
s3 = int(input())
s4 = int(input())
s5 = int(input())
target = int(input())
grade = 1

# 5명의 점수 리스트 생성
scores = [s1, s2, s3, s4, s5]
target_score = scores[target -1]

# target - 1 번째 점수를 비교해서 점수가 더 크면 등수 + 1 
for score in scores:
    if score > target_score:
        grade += 1

# 결과 출력
print(f"{target}번 학생 점수: {target_score}")
print(f"석차: {grade}등")