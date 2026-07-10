# if문 사용해서 입력받은 name이 명단에 있는지 확인하고 결석, 출석 판별하기
attendance = ["윤서", "민준", "도윤", "예준"]
name = input()

# 명단에 없으면 "결석", 있으면 "출석" 출력
print("결석" if name not in attendance else "출석")