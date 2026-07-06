N = int(input())

# 10부터 N까지 반복
for num in range(10, N + 1):
    # 숫자를 리스트로 변환
    num_str = str(num)
    
    # 인덱스 번호 i와 i + 1, 각각의 숫자가 모두 [i] < [i + 1]이면 출력 
    is_increasing_num = all(num_str[i] < num_str[i + 1] for i in range(len(num_str) - 1))
    if is_increasing_num:
        print(num)