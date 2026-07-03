genre = input().strip()
age = int(input())

recommend_movie = {
    "액션" : { "adult": "존 윅", "minor": "스파이더맨"},
    "로맨스" : { "adult": "노트북", "minor": "너의 이름은"}
}

# 영화 추천: 장르 -> 나이 순으로 확인
# 장르 별 나이 별 영화 추천
if genre in recommend_movie:
    if age >= 19:
        age_grade = "adult"
    else:
        age_grade = "minor"
    print(f"추천: {recommend_movie[genre][age_grade]}")
# 그 외 장르 추천 영화 없음 메시지 출력
else:
    print("해당 장르의 추천 영화가 없습니다.")