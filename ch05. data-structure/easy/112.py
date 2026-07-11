name = input()
opt = input()

# 정렬 옵션에 따라 폭 지정 후 출력
# 왼쪽 정렬
if opt == "L":
    print(f"|{name:<10}|")
# 오른쪽 정렬
elif opt == "R":
    print(f"|{name:>10}|")
# 가운데 정렬
elif opt == "C":
    print(f"|{name:^10}|")
# 그 외는 에러
else:
    print("지원하지 않는 옵션입니다.")