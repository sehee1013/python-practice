# 각 줄을 `split(",", 1)` 으로 이름과 동아리 부분 분리. 동아리 부분에 `split()` 적용 (빈 문자열 → []).
n = int(input())
# 딕셔너리 기본값은 list
std_clubs = {}

# n번 이름, 동아리1, 동아리2,... 형식으로 입력 받기
for _ in range(n):
    name, clubs = input().split(',', 1)
    # name, clubs 딕셔너리 저장
    std_clubs[name] = clubs.split()

# 조회 학생 입력 받기
target = input()

# 조회 학생이 없으면 학생 없음
if target not in std_clubs:
    print("학생 없음")
# 동아리 없으면 가입 없음
elif not std_clubs[target]:
    print("가입 없음")
# 조회 학생 동아리 가나다순 정렬하여 공백 구분 한 줄 출력
else:
    print(' '.join(sorted(std_clubs[target])))