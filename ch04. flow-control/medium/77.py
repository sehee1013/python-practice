user = int(input())
computer = 2

# 전략: 1, 2, 3 중의 정수를 입력 받았는지, 승부 결과 순으로 판별

# 결과 딕셔너리 생성
result_dict = {
    1: {"choice": "가위", "msg": "아쉽게도 졌습니다. 😢"},
    2: {"choice": "바위", "msg": "무승부입니다! 😐"},
    3: {"choice": "보", "msg": "축하합니다! 당신이 이겼습니다! 🎉"}
}

 
if user in result_dict:
    print(f'당신: {result_dict[user]["choice"]} / 컴퓨터: 바위')
    print(f'{result_dict[user]["msg"]}')
else: 
    print("잘못된 입력입니다. 1, 2, 3 중에서 선택하세요.")