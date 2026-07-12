from collections import defaultdict
words = input().split()

# 딕셔너리 디폴트는 리스트
length_dict = defaultdict(list)

# 각 단어 순회하며 길이를 키로 딕셔너리에 추가
for word in words:
    # 키값으로 단어 추가
    length_dict[len(word)].append(word)

# 길이 오름차순 정렬하기
for length in sorted(length_dict):
    # 한 줄씩 출력
    print(f"{length}: {' '.join(length_dict[length])}")