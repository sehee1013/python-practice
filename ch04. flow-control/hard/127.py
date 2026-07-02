# 1부터 N 사이의 카프리카 수를 찾아 출력하세요.
n = int(input())

print("카프리카 수:")
# 1부터 N까지 반복
for num in range(1, n + 1):
    # 1인 경우는 1만 출력
    if num == 1:
        print(num)
    else:
        # num의 제곱값 구하고 문자열로 변환
        num_by_num = num ** 2
        str_num_by_num = str(num_by_num)
        
        # 길이 구하고, 길이 // 2 변수 선언, 제곱근 두 부분으로 나누었을 때의 숫자들 변수 선언
        center = len(str_num_by_num)//2
        left_nbn = num_by_num // (10 ** center)
        right_nbn = num_by_num % (10 ** center)
        
        # 제곱값을 (10 ** length)로 나눴을 때의 몫과 나머지를 더한 값이 제곱값과 같다면 출력
        if left_nbn + right_nbn == num and right_nbn != 0:
            if left_nbn < 10:
                print(f"{num}: {num}^2 = {num_by_num}, {left_nbn} + {right_nbn} = {num}")
            else:
                print(f"{num}: {num}^2 = {num_by_num}, {left_nbn} + {right_nbn:02} = {num}")