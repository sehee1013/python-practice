text = input()
result = []

# 문자열 끝날 때까지 반복
for idx in range(len(text)):
    # 인덱스 번호 0 또는 len -1일 때 글자 그대로. 나머지는 *로 변경
    if idx == 0 or idx == len(text) - 1:
        result.append(text[idx])
    else:
        result.append("*")

# 결과 출력
print("마스킹 결과:","".join(result))