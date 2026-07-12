n = int(input())

seen = set()
twice = set()

# n번 동안 반복
for _ in range(n):
    # 이름 입력 받기
    name = input()
    # 처음 보면 seen에 추가
    if name not in seen:
        seen.add(name)
    # 이미 seen에 있으면 twice에 추가
    else:
        twice.add(name)

# 중복이 있으면 정렬 후 공백 구분하여 출력
if twice:
    print(*sorted(twice))
# 없으면 "중복 없음" 메시지 출력
else:
    print("중복 없음")