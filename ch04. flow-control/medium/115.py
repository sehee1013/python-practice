# 월/일 조합으로 별자리 판별
month = int(input())
day = int(input())
sign = ""
# 운세 문구 딕셔너리 만들기
signs = {
    "물병자리": "창의적인 아이디어가 떠오르는 날이에요!",
    "물고기자리": "감성이 풍부해지는 하루입니다!",
    "양자리": "도전하면 좋은 결과가 있어요!",
    "황소자리": "꾸준한 노력이 빛을 발해요!",
    "쌍둥이자리": "소통이 활발해지는 날이에요!",
    "게자리": "새로운 만남이 기다리고 있어요!",
    "사자자리": "리더십을 발휘할 기회가 와요!",
    "처녀자리": "꼼꼼함이 행운을 가져다줘요!",
    "천칭자리": "균형 잡힌 판단이 중요한 날이에요!",
    "전갈자리": "자신감을 가지면 좋은 일이 생겨요!",
    "사수자리": "모험을 즐기면 행운이 따라와요!",
    "염소자리": "성실함이 큰 보상을 가져다줘요!",
}
# 월/일로 별자리 판별
# 1월인 경우
if month == 1:
    if day <= 19:
        sign = "염소자리"
    else:
        sign = "물병자리"
# 2월인 경우
elif month == 2:
    if day <= 18:
        sign = "물병자리"
    else:
        sign = "물고기자리"
# 3월인 경우
elif month == 3:
    if day <= 20:
        sign = "물고기자리"
    else:
        sign = "양자리"
# 4월인 경우
elif month == 4:
    if day <= 19:
        sign = "양자리"
    else:
        sign = "황소자리"
# 5월인 경우
elif month == 5:
    if day <= 20:
        sign = "황소자리"
    else:
        sign = "쌍둥이자리"
# 6월인 경우
elif month == 6:
    if day <= 21:
        sign = "쌍둥이자리"
    else:
        sign = "게자리"
# 7월인 경우
elif month == 7:
    if day <= 22:
        sign = "게자리"
    else:
        sign = "사자자리"
# 8월인 경우
elif month == 8:
    if day <= 22:
        sign = "사자자리"
    else:
        sign = "처녀자리"
# 9월인 경우
elif month == 9:
    if day <= 22:
        sign = "처녀자리"
    else:
        sign = "천칭자리"
# 10월인 경우
elif month == 10:
    if day <= 22:
        sign = "천칭자리"
    else:
        sign = "전갈자리"
# 11월인 경우
elif month == 11:
    if day <= 21:
        sign = "전갈자리"
    else:
        sign = "사수자리"
# 12월인 경우
elif month == 12:
    if day <= 21:
        sign = "사수자리"
    else:
        sign = "염소자리"

# 결과 출력
print(f"당신의 별자리는 {sign}입니다!")
print(f"오늘의 운세: {signs[sign]}")