scores = {"윤서": 85, "지우": 92, "민준": 65, "서윤": 78, "도윤": 95}
name = input()

# 딕셔너리에 있으면 "있음", 없으면 "없음" 출력
if name in scores:
    print("있음")
else:
    print("없음")