text = input()
sub = input()

# sub이 text 안에 있으면 '포함' 출력
if sub in text:
    print("포함")
# 없으면 '미포함' 출력
else:
    print("미포함")