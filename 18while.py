# while
# 조건이 참일동안 반복을 실행하는 문장
# 주로 언제 끝날지 명확하게 정해지지 않은 반복에 사용

# while 조건 :
#   반복실행할문장

# ex) Hello, World!! 를 5번 출력하기
# for _ in range(1, 5+1):
#       print('Hello, World!!')

i = 1                   # 초기화
while i <= 5:           # 반복 조건식
    print('Hello, World!!')
    i = i + 1           # 증감식

# ex) 1 ~ 100 사이 정수 중
# 3의 배수지만, 2의 배수가 아닌 정수 출력
# 또한, 누적합도 계산해서 출력
i = 1
sum = 0
while i <= 100:
    if i % 3 == 0 and i % 2 != 0:
        sum += i
        print(i, end = ' ')
    i += 1
print(sum)

# ----

i = 3
sum = 0
while i <= 100:
    if i % 2 != 0:
        sum += i
        print(i, end = ' ')
    i += 3

print(sum)

# ---
# 만일, 조건식이 언제나 참이라면? - 무한루프

i = 1
while True:
    print(i, end=' ')
    i += 1
