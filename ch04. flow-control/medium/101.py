text = input().lower()
vowel_count = 0
# 모음 리스트 생성
vowel_list = ['a', 'e', 'i', 'o', 'u']

# 문자열 끝날 때까지 반복
for char in text:
    # 문자가 모음 리스트에 있으면 count + 1
    if char in vowel_list:
        vowel_count += 1

# 결과 출력
print("모음 개수:", vowel_count)