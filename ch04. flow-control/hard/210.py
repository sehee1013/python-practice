# 5개 숫자를 입력받아 5x5 빙고판에서 해당 숫자를 X로 표시하세요.
# 숫자 입력 받기
input_nums = [int(input()) for _ in range(5)] 

num = 1

# 5행 5열 출력
for row in range(5):
    for col in range(5):

        # 입력된 숫자와 다른 숫자는 그대로 출력
        if num not in input_nums:
            print(num, end="\t")

        # 입력된 숫자와 같으면 x 출력
        else:
            print("X", end="\t")

        num += 1
        
    # 줄바꿈
    print()