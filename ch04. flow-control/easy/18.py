age = int(input())

# 7세 이하: 무료, 0원
if age <= 7:
    age_class = "무료"
    fee = 0
# 8~13세: 어린이, 5000원
elif age <= 13:
    age_class = "어린이"
    fee = 5000
# 14~19세: 청소년, 8000원
elif age <= 19:
    age_class = "청소년"
    fee = 8000
# 20~64세: 성인, 12000원
elif age <= 64:
    age_class = "성인"
    fee = 12000
# 65세 이상: 경로, 5000원
else:
    age_class = "경로"
    fee = 5000

# 나이, 구분, 요금 출력
print(f"나이: {age}세\n구분: {age_class}\n요금: {fee}원")