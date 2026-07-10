n = int(input())
scores = {}

# n번 동안 이름과 점수를 입력 받기를 반복
for _ in range(n):
    
    # 이름 입력 받기
    name = input()
    # 점수 입력 받기
    score = int(input())

    # 딕셔너리에 저장
    scores[name] = score

# 키와 키 값 다 출력할 때까지 반복
for name in scores:
    # 이름, 성적 출력
    print(f"{name}: {scores[name]}")