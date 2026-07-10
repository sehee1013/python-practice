n = int(input())
words = set()

# n번 동안 단어 입력 받기
for _ in range(n):
    # 단어 입력 받기
    word = input() 
    # set에 추가
    words.add(word)

# 정렬하여 일관된 출력 유지
words = sorted(words)

# 결과 출력
print(" ".join(words))