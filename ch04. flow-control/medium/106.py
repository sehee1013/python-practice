# 뒤집은 문자열과 원본을 비교
text = input()
reversed_text = ""

# 입력받은 문자열 뒤집고 저장
reversed_text = text[::-1]

# text와 같은지 비교하고 판별 결과 출력
if text == reversed_text:
    print(f"{text}은(는) 회문입니다!")
else:
    print(f"{text}은(는) 회문이 아닙니다.")