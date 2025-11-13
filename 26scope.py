# 변수의 유효범위 scope
# 변수나 이름이 유효하게 접근할 수 있는 범위
# 어떤 변수가 어디에서 사용가능한지
# 어디서 접근할 수 없는지를 결정하는 규칙
# 파이썬의 scope : LEGB

# 지역local 변수
# 함수 내에 정의된 변수는 기본적으로 지역변수
# 따라서, 함수내에서만 유효하고 함수를 벗어나면 사라짐

def greeting():
    msg = 'World'
    print(f'Hello,{msg}!!!')

greeting()

# 전역 global 변수
# 함수 밖에 정의된 변수는 기본적으로 전역 변수
# 따라서, 함수 내에서도 접근 가능

message = 'Hello, Python'

def greeting2():
    print(message)

greeting2()

# 단! 전역변수는 함수내에서 값을 수정하더라도
# 함수 밖을 벗어나면 원래 값으로 되돌아 감!!

x, y = 3, 5

def swap(a, b):
    c = b
    b = a
    a = c
    print('함수 내부: ', a, b)

print('함수 호출 전: ', x, y)
swap(x, y)
print('함수 호출 후: ', x, y)

# 한편, 함수 안에서 전역변수를 직접 변경하려면
# global이라는 키워드를 사용해야 함!

def swap2():
    global x, y
    z = y
    y = x
    x = z
    print('함수 내부: ', x, y)

print('함수 호출 전: ', x, y)
swap2()
print('함수 호출 후: ', x, y)
