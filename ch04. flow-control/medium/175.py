# 나이로 기본 요금을 정하고, 오후면 50% 추가
age = int(input())
time_slot = input()

# 나이별 기본 요금 판별
if age <= 7:
    price = 0
elif age <= 13:
    price = 3000
elif age <= 18:
    price = 5000
else:
    price = 8000

# 시간대 오후면 할증 50% 추가
if time_slot == "오후":
    price = price * 3 // 2

# 결과 출력
print(f"나이: {age}세 | 시간대: {time_slot}")
print(f"입장료: {price}원")