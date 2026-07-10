# 끝 N개를 자르는 것은 음수 인덱스 슬라이싱 `lst[:-N]` 으로 가능합니다.
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
skip_num = int(input())

# 끝에 skip_num개를 제외한 나머지 원소 추출하여 출력
print(" ".join(map(str, data[:-skip_num])))