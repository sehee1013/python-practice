scores = [85, 70, 92, 95, 88, 100, 65, 90, 85, 95]

# 허용 점수들 공백 기준으로 구분하여 정수 변환 후 set 만들기
allow_scores = set(map(int, input().split()))
count = 0

# 리스트 순회하여 리스트 안에서 허용 점수 개수 카운트
for score in scores:
    if score in allow_scores:
        count += 1

# 결과 출력
print(count)