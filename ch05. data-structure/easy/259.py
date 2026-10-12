# 슬라이싱은 인덱스 범위를 벗어나도 빈 리스트를 돌려주기 때문에 양 끝 경계도 그냥 처리할 수 있습니다.
n = int(input())

# n개의 점수 입력 받기
scores = [int(x) for x in input().split()]
# 인덱스 i 입력 받기
del_idx = int(input())

# 인덱스 i인 요소 제거 후 결과 출력
filtered_scores = scores[:del_idx] + scores[del_idx + 1:]

print(" ".join(map(str, filtered_scores)))