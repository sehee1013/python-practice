# 리스트 멤버십 검사에는 `in` 연산자를 사용
members = ["윤서", "지우", "민준", "서윤", "도윤"]
name = input()

# 리스트 멤버십에 있으면 "있음", 없으면 "없음" 출력
print("있음" if name in members else "없음")