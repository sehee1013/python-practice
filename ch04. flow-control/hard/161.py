mode = int(input())
shift = int(input())
text = input()
result = ""

# 인코딩인 경우
if mode == 1:
    # text의 한 글자씩 순회
    for char in text:

        # 유니코드로 변환
        ord_char = ord(char)

        # 알파벳인 경우 해독 진행
        if 65 <= ord_char <= 90 or 97 <= ord_char <= 122:
            # 변환 후 + shift
            changed_ord_char = ord_char + shift

            # 만약 더한 값이 65에서 90(대문자) 또는 97에서 122 사이(소문자)가 아니라면
            # 코드값이 122보다 크고 원래 소문자인 경우
            if changed_ord_char > 122 and ord_char >= 97:
                # changed_char - 122
                changed_ord_char = (changed_ord_char - 122) + 96

            # 코드값이 90보다 크고 원래 대문자인 경우
            elif changed_ord_char > 90 and ord_char <= 90:
                changed_ord_char = (changed_ord_char - 90) + 64
            
            # 바꾼 결과 리스트에 추가하기
            result += chr(changed_ord_char)
        
        # 알파벳이 아닌 경우 그대로 추가
        else:
            result += char

# 디코딩인 경우
elif mode == 2:
    # text의 한 글자씩 순회
    for char in text:

        # 유니코드로 변환
        ord_char = ord(char)

        # 알파벳인 경우 해독 이어서 진행
        if 65 <= ord_char <= 90 or 97 <= ord_char <= 122:
            # 변환 후 - shift
            changed_ord_char = ord_char - shift

            # 만약 뺀 값이 65에서 90 또는 97에서 122 사이가 아니라면
            # 97보다 작고 원래 소문자인 경우 
            if changed_ord_char < 97 and ord_char >= 97:
                changed_ord_char = 123 - (97 - changed_ord_char)
            # 코드값이 65보다 작고 원래 대문자인 경우
            elif changed_ord_char < 65 and ord_char <= 90:
                changed_ord_char = 91 - (65 - changed_ord_char)
            
            # 바꾼 결과 리스트에 추가하기
            result += chr(changed_ord_char)

        # 알파벳이 아닌 경우 그대로 추가
        else:
            result += char

# 결과 출력
print("결과:", result)
