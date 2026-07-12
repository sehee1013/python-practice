words = input().split()
frequency = dict()

# words 순회하며 각 단어 접근
for word in words:
    # 빈도 딕셔너리에 이미 있으면 + 1, 없으면 새롭게 추가
    frequency[word] = frequency.get(word, 0) + 1

# 개수, 이름 튜플 리스트 생성
sorted_freq = [(-count, name) for name, count in frequency.items()]

# 정렬 후 상위 3개의 단어만 추출
sorted_freq.sort()
top_3 = sorted_freq[:3]

# 공백 구분하여 출력
print(" ".join(name for _, name in top_3))