usage = int(input())

# 사용량 100 이하
if usage <= 100:
    charge = usage * 60
# 사용량 100 초과 200 이하
elif usage <= 200:
    charge = 100 * 60 + (usage - 100) * 120
# 사용량 200 초과
else:
    charge = 100 * 60 + 100 * 120 + (usage - 200) * 190

# 부과세 구하기
tax = int(charge * 0.1)
total = charge + tax

# 결과 출력
print(f"전기 요금: {charge}원")
print(f"부가세 (10%): {tax}원")
print(f"총 납부 금액: {total}원")