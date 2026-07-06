s1 = input()
s2 = input()
result = []

# s1과 s2 중 길이가 작은 것의 길이만큼 반복
for idx in range(min(len(s1), len(s2))):
    # s[idx]을 반복해서 넣기
    result.append(s1[idx])
    result.append(s2[idx])

min_len = min(len(s1), len(s2))

# 긴 것의 나머지 문자열 넣기
if len(s1) > len(s2):
    result.append(s1[min_len:])
elif len(s2) > len(s1):
    result.append(s2[min_len:])

# 결과 출력 
print("".join(result))