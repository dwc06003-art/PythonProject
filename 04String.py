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

# 문자열 비교 - 문자열 풀(pool)
# 동일한 문자열 값을 한번만 저장하고 재사용하는 매커니즘
# 즉, 같은 문자열을 메모리에 여러번 생성하지 않음 - 메모리 절약
say1 = 'Hello, World!!'
say2 = 'Hello, World!!'
print(say1 == say2)
print(id(say1), id(say2))   # 메모리 위치 비교

say3 = str('Hello, World!!')
print(say1 == say3)
print(id(say1), id(say3))

say4 = say1[:]  #슬라이싱을 통한 문자열 복사
# say4 = "".join([say1])
print(say1 == say4)
print(id(say1), id(say4))

# 시퀀스(sequence) 자료형
# 값들이 순서대로 나열되어 있고
# 이 값들을 인덱스(위치)로 접근할 수 있는 자료형
# 단, 위치는 0부터 차례대로 부여되어 있음
# 인덱싱, 슬라이싱, 순회 연산이 공통으로 제공
# 문자열, 리스트, 튜플

# 인덱싱(indexing)
# 시퀀스 안에 있는 개별 요소를 하나씩 꺼내는 방법
# 각 요소가 순서대로 저장되어 있으므로
# 그 번호를 이용해서 요소에 접근할 수 있음
# 변수명[인덱스]

str1 = "Hello, World!!"
print(str1[0], str1[5], str1[10])
#print(str1[99])     # 인덱스 범위를 벗어남 - 오류 발생!
print(str1[5], str1[-5])

# 인덱스를 이용해서 요소 바꾸기
# 문자열 시퀀스는 불변객체이기 때문에
# 한번 만들어지면,개별 요소(내용)는 수정할 수 없음
# str1[0] = 'A'   # 수정불가 - 대입연산 불가

print('수정전', id(str1))
str1 = str1 + "and greeting!!"
print('수정후', id(str1))

# 문자열 슬라이싱
# 시퀀스형 자료에서 구간(부분)을 잘라내는 연산
# 시퀀스[시작:끝-1:간격]

str1 = "Hello, World!!"
# 'Hello'라는 문자열만 출력
print(str1[0], str1[1], str1[2], str1[3], str1[4], sep = '')
print(str1[0:5], str1[:5] )
# 'World'라는 문자열만 출력
print(str1[7:12])
# 'World!!'라는 문자열만 출력
print(str1[7:14], str1[7:])

# ex) 주민번호를 이용해서 성별을 출력하는 코드
jumin = '123456-1234567'

result ='남' if (jumin[7] == '1') else '여'
print(jumin , result)

# 시퀀스 길이 연산
# len(시퀀스) - 요소의 갯수 출력
print(str1, len(str1))