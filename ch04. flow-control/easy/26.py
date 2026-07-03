is_member = input().strip()

# 할인 적용: 회원 여부 -> VIP 여부 순으로 확인
# 회원인 경우 10%, VIP는 20% 할인 적용, 회원 아니면 할인 없음
if is_member == "Y":
    is_vip = input().strip()
    if is_vip == "Y":
        print("20% 할인 적용")
    else:
        print("10% 할인 적용")
else: 
    print("할인 없음")