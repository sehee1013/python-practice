s1 = {"윤서": 85, "지우": 92, "민준": 65}
s2 = {"지우": 88, "민준": 70, "도윤": 95}
name = input()

# 양쪽 모두에 있으면 변화 표시 (s2 - s1)
if name in s1 and name in s2:
    gap = s2[name] - s1[name]
    if gap > 0:
        print(f"변화: +{gap}")
    else:
        print(f"변화: {gap}")
# 한쪽에만 있으면 '한 학기만'
elif name in s1 or name in s2:
    print("한 학기만")
# 양쪽 모두에 없으면 '없음'
else:
    print("없음")