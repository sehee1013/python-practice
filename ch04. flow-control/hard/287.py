# 평균을 먼저 구한 뒤, 인덱스 순회하며 조건 만족 시 "번호-점수" 형식으로 한 줄에 이어 출력하세요.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]

# 평균 구하기
average = sum(scores) / len(scores)

# 리스트 중 평균보다 큰 경우 인덱스 번호와 함께 출력
for idx, score in enumerate(scores):
    if score > average:
        print(f"{idx + 1}-{score}", end=" ")