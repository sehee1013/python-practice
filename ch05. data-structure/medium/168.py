n = int(input())
counts = {}

# n번 이름 입력 받기
names = [input() for _ in range(n)]

# 학생들의 등록 횟수 딕셔너리 만들기
for name in names:
    counts[name] = counts.get(name, 0) + 1

# 키 값이 2 이상인 경우만 딕셔너리 추가하고 정렬
sorted_duplicate = {name: count for name, count in sorted(counts.items()) if count >= 2}

# 이름 한 줄씩 출력
if sorted_duplicate:
    for name, count in sorted_duplicate.items():
        print(f"{name}: {count}회")
# 중복 없으면 '중복 등록 없음' 출력
else:
    print("중복 등록 없음")