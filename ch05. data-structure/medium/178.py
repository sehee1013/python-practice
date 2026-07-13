text = set(input().split())
queries = input().split()
including = []
non_including = []

# 검색어 list 순회
for word in queries:
    # 본문에 있으면 포함 리스트 추가
    if word in text:
        including.append(word)
    # 본문에 없으면 비포함 리스트 추가
    else:
        non_including.append(word)
        
# 결과 출력
print(f"포함: {' '.join(sorted(including))}")
print(f"미포함: {' '.join(sorted(non_including))}")