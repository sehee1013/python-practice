url = input()

# 'http://' 또는 'https://'가 있으면 제거
if url.startswith('http://'):
    url = url[len('http://'):]
elif url.startswith('https://'):
    url = url[len('https://'):]

# 첫 '/' 위치 구하기
slash_index = url.find('/')

# 첫 '/' 위치 기준으로 도메인, 경로 구하기('/'없으면 경로: '/')
if slash_index != -1:
    domain, path = url[:slash_index], url[slash_index:]
else:
    domain, path = url, '/'

# 결과 출력
print("도메인:", domain)
print("경로:", path)