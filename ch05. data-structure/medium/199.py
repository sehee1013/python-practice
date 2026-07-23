# `endswith` 와 슬라이싱 `w[:-3]`, `w[:-2]` 로 접미사 제거
words = input().split()

# 추출하는 함수 정의
def stem_word(word):
    # 'ing'로 끝나고 길이가 4 이상이면 마지막 ing 제거
    if word.endswith('ing') and len(word) >= 4:
        return word[:-3]
    # 또는 ed로 끝나고 길이가 3 이상이면 마지막 ed 제거
    elif word.endswith('ed') and len(word) >= 3:
        return word[:-2]
    # 그 외는 그대로
    return word

# 결과 출력
print(' '.join(stem_word(word) for word in words))