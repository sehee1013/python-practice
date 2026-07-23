# 두 단어를 각각 set 으로 변환 → `&` 교집합 → 정렬 → join.
first_word = input()
second_word = input()

# 두 단어 set으로 변환
first_set = set(first_word)
second_set = set(second_word)
 
# 교집합으로 공통 글자 구하기
common = first_set & second_set

# 정렬하여 한 줄 출력(공통 글자 없으면 '공통 없음' 출력)
print(''.join(sorted(common)) if common else '공통 없음')