# 문자열 다루기

# 문자열 포매팅 사용하기 전
print('Hello, World~!!')
print('Hello, Python~!!')
# ----
say = 'World'
print('Hello, ' + say + '~!!')
say = 'Python'
print('Hello, ' + say + '~!!')

# 문자열 포매팅 1 - %
print('Hello, %s~!!' % say)
name, weight, age = '홍길동', 55.5, 35
print('이름 : %s, 몸무게 : %.1fkg, 나이 : %d' % (name, weight, age))

# 문자열 포매팅 2 - .format
print('Hello, {0}~!!'.format(say))
print('이름 : {}, 몸무게 : {:.2f}kg, 나이 : {}' .format(name, weight, age))

# 문자열 포매팅 3 - f포매팅 (3.6이상, 추천!)
print(f'Hello, {say}~!!')
print(f'이름 : {name}, 몸무게 : {weight:.2f}kg, 나이 : {age}')
# 문자열 슬라이싱