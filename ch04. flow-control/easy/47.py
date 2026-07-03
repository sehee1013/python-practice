total = 0
count = 0

# num 입력 받기
num = int(input())
 
# num이 0이 아닌 동안 반복
while num != 0:
    total += num
    count += 1
    
    # num 반복 입력
    num = int(input())

# 입력한 숫자가 하나도 없으면 경고 메시지 출력, 입력값 있으면 평균 구해서 출력
if count == 0 and num == 0:
    print("입력한 숫자가 없습니다.")
else:
    average = total / count
    
    print(f"평균: {average}")
