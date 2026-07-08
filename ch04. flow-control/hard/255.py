# 3x3 격자의 숫자가 1~9를 모두 포함하는지 검증하세요.
has1 = False
has2 = False
has3 = False
has4 = False
has5 = False
has6 = False
has7 = False
has8 = False
has9 = False

print("--- 3x3 검증 ---")
# 3 x 3 입력 받기
for _ in range(3):
    nums = input().strip()

    print("".join(nums))
    # nums 안의 num에 해당하는 숫자 플래그 True로 갱신
    for num in nums:
        if "1" == num:
            has1 = True
        elif "2" == num:
            has2 = True
        elif "3" == num:
            has3 = True
        elif "4" == num:
            has4 = True
        elif "5" == num:
            has5 = True
        elif "6" == num:
            has6 = True
        elif "7" == num:
            has7 = True
        elif "8" == num:
            has8 = True
        elif "9" == num:
            has9 = True

# 결과 출력
if has1 and has2 and has3 and has4 and has5 and has6 and has7 and has8 and has9:
    print("결과: 유효합니다!")
else:
    print("결과: 유효하지 않습니다!")