words = input().split()

# 중복 제거하기
set_words = set(words)

# 정렬하여 최종 리스트 생성
result = sorted(set_words)

# 결과 출력
print(f"종류: {len(result)}")
print(" ".join(result))