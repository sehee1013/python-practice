club_a = {"윤서", "지우", "민준", "도윤"}
club_b = {"지우", "민준", "예준", "하준"}
name = input()

# 양쪽 모두에 있는 경우
if name in club_a and name in club_b:
    print("양쪽 모두")
# A 동아리만 있는 경우
elif name in club_a:
    print("A 동아리만")
# B 동아리만 있는 경우
elif name in club_b:
    print("B 동아리만")
# 둘 다 없는 경우
else:
    print("미가입")