# `lst[a:b]` 은 인덱스 a부터 b-1까지의 원소를 새 리스트로 반환합니다.
scores = [85, 92, 78, 95, 88, 70, 100, 65, 82, 90]
a = int(input())
b = int(input())

# 슬라이싱으로 구간 별 점수 추출
# 결과 출력
print(" ".join(map(str, scores[a:b])))