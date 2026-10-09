# 앞 두 토큰=단어 리스트 pair, 나머지 key=value=옵션 dict opts.
# 예: "hello world sep=_ end=?" → pair=["hello","world"], opts={"sep":"_","end":"?"}
tokens = input().split()
pair = tokens[:2]
opts = {}
for token in tokens[2:]:
    k, v = token.split("=")
    opts[k] = v

# 아래 함수는 이미 정의되어 있습니다 (수정하지 마세요).
def make(a, b, sep="-", end="!"):
    return a + sep + b + end

# pair와 opts 언패킹 후 make 함수 호출하여 그 반환값 출력
print(make(*pair, **opts))