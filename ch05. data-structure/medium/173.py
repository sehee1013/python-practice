words = input().split()
word_count = {}
dupli_dict = {}

# words 순회하며 딕셔너리 추가하기
for word in words:
    # 단어가 이미 딕셔너리 키로 존재하는 경우 키값 + 1
    word_count[word] = word_count.get(word, 0) + 1

# 딕셔너리 순회하며 출력
for key in word_count:
    # 2회 이상 등장하는 경우만 중복 딕셔너리 추가
    # 문제에서 입력 데이터는 2회 이상 등장하는 단어들의 빈도가 서로 다르도록 보장하므로 가능
    if word_count[key] >= 2:
        dupli_dict[word_count[key]] = key
        
# 중복이 있는 경우 빈도순 정렬하여 출력
if dupli_dict:
    for key in dupli_dict:
        print(f"{dupli_dict[key]}: {key}")
# 중복 없으면 메시지 출력
else:
    print("중복 없음")