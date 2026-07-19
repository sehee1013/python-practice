n = int(input())
words = {}

# n번 단어:정의 형식으로 입력 받기
for _ in range(n):
    word, definition = input().split(":")
    words[word] = definition

# 조회할 단어 query 입력 받기
query = input()

# query가 있으면 값 출력, 없으면 '없음' 출력
print(words.get(query, '없음'))