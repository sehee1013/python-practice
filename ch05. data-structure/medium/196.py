# dict 빌딩 후 조회 + if/elif 로 등급 결정.
n = int(input())
members = {}

# name, point 형식으로 n번 입력 받기
for _ in range(n):
    name, point_str = input().split(',')
    
    # 딕셔너리에 저장
    members[name] = int(point_str)

# 조회할 회원 이름 query 입력 받기
query = input()

# 존재하는 회원인 경우 포인트로 등급 산출
if query in members:
    point = members[query]

    if point >= 10000:
        grade = 'VIP'
    elif point >= 5000:
        grade = 'GOLD'
    elif point >= 1000:
        grade = 'SILVER'
    else:
        grade = 'BRONZE'

    # 결과 출력
    print(f"{query}: {grade} ({point}점)")
# 회원이 없으면 '회원 없음' 출력
else:
    print("회원 없음")