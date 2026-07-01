month = int(input())

seasons = {
    "봄" : "따뜻한 봄이에요! 꽃구경 가세요 🌸",
    "여름" : "더운 여름이에요! 시원하게 보내세요 🌊",
    "가을" : "선선한 가을이에요! 단풍 구경 가세요 🍂",
    "겨울" : "추운 겨울이에요! 따뜻하게 입으세요 ⛄️"
}
#월별 계절 판별, 계절 인사 출력
if month == 3 or month == 4 or month == 5:
    season = "봄"
elif month == 6 or month == 7 or month == 8:
    season = "여름"
elif month == 9 or month == 10 or month == 11:
    season = "가을"
elif month == 12 or month == 1 or month == 2:
    season = "겨울"
else:
    season = ""
    print("잘못된 입력입니다.")

if season in seasons:
    print(f"{season}입니다.")
    print(f"{seasons[season]}")