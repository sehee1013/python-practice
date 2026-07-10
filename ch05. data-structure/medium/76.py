words = input().split()

# 빈 딕셔너리 생성
counts = {}
for word in words:
    # 각 단어의 등장 횟수 세기
    counts[word] = counts.get(word, 0) + 1

# 첫 등장 순서대로 출력
for word in counts:
    print(f"{word}: {counts[word]}")