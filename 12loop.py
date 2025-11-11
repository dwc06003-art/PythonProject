# 반복문
# 정해진 횟수나 조건에 따라
# 특정코드를 반복으로 실행하도록 만든 문장

# 만일, Hello, World!!를 1번 출력한다면?
# => print함수 1번만 사용
print('Hello, World!!')

# Hello, World!!를 3번 출력한다면?
print('Hello, World!!')
print('Hello, World!!')
print('Hello, World!!')

# 만일, 100번 출력해야 한다면? - 복붙을 계속할 것인가?
# 단, 반복시 출력해야 하는 문구가 바뀌면? - 다시 수정 - 번거로움!
# 효율적인 반복실행을 위해 반복문을 사용함!

# ex) 1~10 까지 출력하기
print(1, end = ', ')
print(2, end = ', ')
print(3, end = ', ')
print(4, end = ', ')
print(5, end = ', ')
print(6, end = ', ')
print(7, end = ', ')
print(8, end = ', ')
print(9, end = ', ')
print(10)

# for 반복
# 정해진 횟수만큼 코드를 반복 실행
# for 반복변수 in range(시작값, 종료값-1, 증감값):
#     반복실행할 문장

# range 함수 사용하기 : 정수 시퀀스 생성
print(range(1, 10))
print(list(range(1, 10)))    # range 객체를 리스트로 변환

# ex) 1~10 까지 출력하기
for i in range(1, 10+1):
    print(i, end = ', ')
print('')   # end = '' 초기화용 코드

# ex) Hello, World!!를 5번 출력하기
for _ in range(1, 5+1):
    print('Hello, World!!')

# ex) 1~100 사이 정수중
# 3의 배수지만, 2의 배수가 아닌 정수 출력
# 또한, 누적합도 계산해서 출력

sum = 0
for i in range(1, 100+1):
    if i % 3 == 0 and i % 2 != 0:
        sum += i
        print(i, end = ' ')
print()
print(sum)

# range의 증감값을 이용해서 반복 횟수를 줄임
for i in range(3, 100+1, 3):
    if i % 2 != 0:
        print(i, end = ' ')
print()

# for문은 유한한 반복을 염두에 두고 설계
# 그래도, 무한루프를 만들고 싶다면 itertools, iter함수를 이용
i = 1
for _ in iter(int, 1):
    if i == 9999999: break
    print(i, end = ' ')
    i += 1
print()


import itertools

for i in itertools.count():
    if i == 99999: break
    print(i, end = ' ')
print()

# for (i = 0; i <=10; ++i) {
#   print(i)
# }

# for (;;) {
#   print(i)
# }