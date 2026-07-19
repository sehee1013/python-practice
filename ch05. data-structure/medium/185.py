# 입력 받기
words = input().strip().lower().split()

# 중복 제거
set_words = set(words)

# 결과 출력
print(" ".join(sorted(set_words)))