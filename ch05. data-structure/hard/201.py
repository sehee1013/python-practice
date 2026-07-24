# enumerate 로 (인덱스, 단어) 순회 + dict[word] 에 위치 list 누적. 출력은 sorted(keys) 순.
from collections import defaultdict

words = input().split()

inverted_index = defaultdict(list)

# 인덱스와 단어 순회하며 각 단어를 키로하여 리스트에 인덱스 추가
for idx, word in enumerate(words):
    inverted_index[word].append(idx)

# 단어 가나다 순으로 정렬하여 결과 한 줄씩 출력
for word in sorted(inverted_index):
    print(f"{word}: {' '.join(map(str, inverted_index[word]))}")