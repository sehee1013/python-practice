# key=value 토큰을 dict 로 파싱합니다. 예: "greeting=안녕 name=철수" → opts={"greeting":"안녕","name":"철수"}
opts = {}
for token in input().split():
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def greet(greeting, name):
    return greeting + ", " + name + "!"

# opts 를 ** 로 풀어 greet 에 넘기고, 그 반환값 출력
print(greet(**opts))