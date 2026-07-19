words = input().split()
count = {}

# 각 단어 빈도 세기
for word in words:
    count[word] = count.get(word, 0) + 1

# 내림차순 정렬
sorted_count = [(-value, key) for key, value in count.items()]

# 결과 출력
for neg_count, word in sorted(sorted_count):
    print(f"{word}: {'*' * -neg_count}")