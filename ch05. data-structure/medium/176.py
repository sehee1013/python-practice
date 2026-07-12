s = input()
count_dict = {}

# 문자열 각 문자 순회
for char in s:
    # 공백 제외
    if char == " ":
        continue
    # 문자 딕셔너리 키로 추가하고 이미 딕셔너리 키로 존재하면 키값 + 1
    count_dict[char] = count_dict.get(char, 0) + 1

# 문자 사전순 정렬하여 결과 출력
for key in sorted(count_dict):
    print(f"{key}: {count_dict[key]}")