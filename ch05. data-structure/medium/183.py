words = input().split()

# 빈도 dict 생성
frequency = {}

# 단어들 순회하며 키 생성, 이미 존재하는 키는 키값 + 1
for word in words:
    frequency[word] = frequency.get(word, 0) + 1

max_count = 0
most_frequent_word = None

# 가장 자주 등장한 단어 구하기
for key, count in frequency.items():
    if count > max_count:
        most_frequent_word = key
        max_count = count

# 결과 출력
print(f"{most_frequent_word}: {max_count}")