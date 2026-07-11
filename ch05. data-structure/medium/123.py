s = input().lower().replace(" ", "")

# 앞뒤로 같은 문자열인지 판별하기
reversed_s = s[::-1]

# 결과 출력
if s == reversed_s:
    print("회문")
else:
    print("회문 아님")