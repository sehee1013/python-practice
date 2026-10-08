# key=value 토큰을 dict 로 파싱합니다. 예: "width=4 height=5" → opts={"width":"4","height":"5"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def box(width, height):
    return width + "x" + height

# opts 를 ** 로 풀어 box 에 넘기고, 그 반환값 출력
print(box(**opts))