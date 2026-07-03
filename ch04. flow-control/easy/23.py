blood = input()

# 성격 딕셔너리  생성
character = {
    "A" : "꼼꼼하고 신중한 성격",
    "B" : "자유롭고 창의적인 성격",
    "O" : "사교적이고 리더십이 강한 성격",
    "AB" : "이성적이고 독창적인 성격"
}

# A,B,O,AB 가 아닌 경우 잘못된 입력 안내 메세지 출력
if blood in character:
    print(f"혈액형: {blood}형") 
    print(f"성격: {character[blood]}") 
else:
    print("잘못된 입력입니다.")
