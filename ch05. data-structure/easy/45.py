# 조건 검사 시 대소문자 차이를 없애려면 `c.lower() in "aeiou"` 가 편합니다.
# 결과를 한 문자열로 이어 붙이려면 `"".join(...)` 을 사용하세요.
s = input()

# 모음 리스트 
vowels = 'aeiou'
# 모음인 경우만 문자열 새 리스트에 저장
result = [char for char in s if char.lower() in vowels]

# 결과 출력
print("".join(result))