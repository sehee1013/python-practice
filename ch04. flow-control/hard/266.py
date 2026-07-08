# 암호 해독: 치환 암호를 복호화하세요.
cipher = input()
key = input()
result = ""

# 알파벳 문자열 생성
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 암호문의 글자 하나씩 순회
for cipher_char in cipher:

    for idx in range(26):
        # 암호문의 글자와 같은 키 글자의 인덱스 번호를 구해서 알파벳으로 해독
        if cipher_char == key[idx]:
            result += alphabet[idx]
            break
    # 알파벳이 아니면 그대로 결과에 추가
    else:
        result += cipher_char

# 결과 출력
print(result)