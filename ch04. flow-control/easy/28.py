written = int(input())

written_pass = 60
practical_pass = 70
# 시험 합격: 필기 점수 -> 실기 점수(필기 60점 이상인 경우만) 순으로 확인
# 필기 60점 이상이면 축하 메시지 출력, 실기 점수 받기
if written >= written_pass:
    print("필기 합격!")
    practical = int(input())
    # 실기 70점 이상 최종 합격
    if practical >= practical_pass:
        print("최종 합격입니다!")
    # 실기 70점 미만 실기 불합격, 실기 재시험 대상
    else:
        print("실기 불합격입니다. 실기 재시험 대상입니다.")
# 필기 60점 미만 필기 불합격,필기 재응시 메시지 출력
else:
    print("필기 불합격입니다. 필기부터 다시 응시하세요.")