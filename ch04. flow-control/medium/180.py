# 좌석번호를 열(A~J)과 번호(1~10)로 변환하세요
seat = int(input())
error = False

# 좌석 번호 범위로 열 부여
if 1 <= seat <= 10:
    row = "A"
elif 11 <= seat <= 20:
    row = "B"
elif 21 <= seat <= 30:
    row = "C"
elif 31 <= seat <= 40:
    row = "D"
elif 41 <= seat <= 50:
    row = "E"
elif 51 <= seat <= 60:
    row = "F"
elif 61 <= seat <= 70:
    row = "G"
elif 71 <= seat <= 80:
    row = "H"
elif 81 <= seat <= 90:
    row = "I"
elif 91 <= seat <= 100:
    row = "J"
# 그 외: 경고 메시지 출력
else:
    print("잘못된 좌석번호입니다.")
    error = True
# 좌석 번호 % 10 값으로 번호 부여
if seat % 10 == 0:
    col = 10
else:
    col = seat % 10

if not error:
    # 결과 출력
    print(f"좌석 {seat} → {row}열 {col}번")