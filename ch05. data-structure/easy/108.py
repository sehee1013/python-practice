text = input()
suffix = input()

# 본문이 suffix로 끝나면 yes 아니면 no 출력
print("yes" if text.endswith(suffix) else "no")