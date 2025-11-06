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

# 문자열 입력받기
# input(입력시 표시할 메세지)
name = input('이름을 입력하세요 : ')
print(name)

# ex) 두 수를 입력받아 사칙연산 후 결과 출력
# input를 통해 입력받은 내용은 기본적으로 문자열
# 입력한 내용을 숫자로 바꾸려면 형변환 함수 필요!
# 형변환 : 데이터의 자료형을 다른 형식으로 바꾸는 것
# 암시적 형변환(프로모션) : 파이썬이 자동으로 변환해 줌
# 명시적 형변환 : 프로그래머가 직접 변환
# int(대상), float(대상), str(대상)
# x = input('사칙연산할 첫번째 순자를 입력하세요 : ')
# y = input('사칙연산할 두번째 순자를 입력하세요 : ')
x = int(input('사칙연산할 첫번째 순자를 입력하세요 : '))
y = int(input('사칙연산할 두번째 순자를 입력하세요 : '))
print(x + y, x - y, x * y, x / y)

# 문자열 슬라이싱