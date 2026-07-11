text = input()
prefix = input()

# 본문이 prefix로 시작하면 yes 출력
if text.startswith(prefix):
    print("yes")
# 아니면 no 출력
else:
    print("no")