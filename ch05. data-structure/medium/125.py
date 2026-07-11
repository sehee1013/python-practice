text = input()
words_count = {}

# 공백 기준으로 구분하여 리스트 변환
words = text.lower().split()

# 리스트 순회하며 단어 딕셔너리 넣기
for word in words:
    # 이미 키가 존재하면 count +1 하기
    words_count[word] = words_count.get(word, 0) + 1

# 가장 자주 등장한 단어 찾아서 변수 할당
max_count = 0
max_word = ""

for word, count in words_count.items():
    # 카운트 큰 거 갱신
    if count > max_count:
        max_count = count
        max_word = word

# 결과 출력
print(f"{max_word}: {max_count}")