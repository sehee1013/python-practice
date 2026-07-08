# 알파벳 1글자를 입력받아 5x5 별 패턴으로 출력하세요.
ch = input().strip().upper()

# 유효한 문자인 경우 해당하는 별 패턴 출력
if ch == "A":
    print(" *** ")
    print("*   *")
    print("*****")
    print("*   *")
    print("*   *")
elif ch == "B":
    print("**** ")
    print("*   *")
    print("**** ")
    print("*   *")
    print("**** ")
elif ch == "C":
    print(" ****")
    print("*    ")
    print("*    ")
    print("*    ")
    print(" ****")
# A, B, C 외 문자가 입력되면 경고 메시지 출력
else:
    print("지원하지 않는 문자입니다.")