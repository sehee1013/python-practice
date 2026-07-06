# for문으로 문자열을 순회하며 플래그를 사용하세요.
s = input()

at = False
dot = False

# 문자열 순회하며 판별
for char in s:
    # @와 . 모두 포함되어 있으면 유효
    if "@" == char:
        at = True
    elif "." == char:
        dot = True

if at and dot:
    print("유효")
else:
    print("무효")