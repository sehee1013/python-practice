# 수를 문자열로 변환하여 뒤집고, 회문 여부를 판단
num = int(input())
turn = 0

# 회문이 될 때까지 무한 반복
while True:
    str_num = str(num)
    # 회문인 경우 탈출
    if str_num == str_num[::-1]:
        break
    else:
        reversed_num = int(str_num[::-1])
        
        # 단계 출력
        print(f"단계 {turn + 1}: {num} + {reversed_num} = {num + reversed_num}")

        # num + num 뒤집은 값으로 갱신
        num = num + reversed_num
        turn += 1

# turn이 0인 경우 출력
if turn == 0:
    print(f"이미 회문입니다: {num}") 
# 아닌 경우
else:
    print(f"회문 완성: {num} ({turn}단계)")