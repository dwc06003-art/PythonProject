# 프로그램의 3대 논리 - 순서, 선택, 반복
# 순차 - 명령어를 위에서 아래로 순서대로 실행
# 선택 - 조건에 따라 실행할 명령어가 달라짐
# 반복 - 같은 명령어를 반복 수행

# 조건문
# 어떤 조건에 따라 프로그램 실행 흐름을 제어하는 문장
# 명령의 분기를 만드는 도구
# 파이썬에서는 if문으로 이용해 조건문을 작성

# 단순 if
# if 조건식 :
#    참일때 실행할명령

# 블록(block)
# 여러 개의 명령문을 하나의 논리적 단위로 묶은 것
# 조건문/반복문에서 조건이 참일때 실행할 코드들을 묶은 부분
# 즉, 여러 줄의 코드를 하나의 실행 단위로 만든 것
# 파이썬에서는 블록을 들여쓰기(indent)로 구분

# ex) 시험 점수가 85점 이상이면 '합격'이라 출려
jumsu = 90
result = '불합격입니다!'  # 결과에 대한 초기값 설정
if jumsu >= 85:
    result = '합격입니다!!'

print(result)

# ex)
rate = float(input('Enter you score : '))
result = '해외 연수 기회는 다음에...'

if rate >= 4.2:
    result = '해외 연수 기회 부여'

print(f'당신의 평점 : {rate}')
print(result)

# 기본 if문
# if 조건식:
#    참일때 실행할명령
# else
#    거짓일때 실행할명령


# ex) 두개의 수를 입력받아 큰 수를 출력
num = int(input('첫 번째 숫자입력 : '))
num2 = int(input('두 번째 숫자입력 : '))

if num > num2:
    result = f'두 수 중에 큰수는 {num}이고 작은 수는 {num2}입니다'
else:
    result = f'두 수 중에 큰수는 {num2}이고 작은 수는 {num}입니다'

print(result)

# 다중 if문
# if 조건식1:
#    조건식1 참일때 실행할명령
# if 조건식2:
#    조건식2 참일때 실행할명령
# else
#    그외 조건일때 실행할명령

# ex) 4-8b 두개의 수를 입력받아 큰 수를 출력
# 같은 수 2개를 입력했을 때 처리하는 코드도 추가
num = int(input('첫 번째 숫자입력 : '))
num2 = int(input('두 번째 숫자입력 : '))

if num > num2:
    result = f'두 수 중에 큰수는 {num}이고 작은 수는 {num2}입니다'
elif num > num:
    result = f'두 수 중에 큰수는 {num2}이고 작은 수는 {num}입니다'
else:
    result = f'입력한 두 수가 같습니다'

print(result)

# ex) 4-9 입력한 두 수의 짝수/홀수 여부 판단
num1 = int(input('첫 번째 숫자입력 : '))
num2 = int(input('두 번째 숫자입력 : '))

is_all_even = num1 % 2 == 0 and num2 == 0
is_all_odd = num1 % 2 != 0 and num2 != 0

if is_all_even:
    result = f'입력한 수 {num1},{num2}는 모두 짝수입니다'
elif is_all_odd:
    result = f'입력한 수 {num1},{num2}는 모두 홀수입니다'
else:
    result = f'입력한 수 {num1},{num2}는 짝수 또는 홀수입니다'

print(result)

# ex) 4-10 과목 점수에 대한 학점 처리
jumsu = int(input('점수를 입력하세요 : '))

# if 90 <= jumsu <=100:
#     result = 'A학점입니다'
# elif 80 <= jumsu < 90:
#     result = 'B학점입니다'
# elif 70 <= jumsu < 80:
#     result = 'C학점입니다'
# elif 60 <= jumsu < 70:
#     result = 'D학점입니다'
# else:
#     result = 'F학점입니다'
#
# print(result)

if jumsu >= 90:
    result = 'A학점입니다'
elif jumsu >= 80:
    result = 'B학점입니다'
elif jumsu >= 70:
    result = 'C학점입니다'
elif jumsu >= 60:
    result = 'D학점입니다'
else:
    result = 'F학점입니다'

print(result)

# 중첩 if문 - if문 속에 또 다른 if문을 작성
# if 조건1:
#    if 조건2:
#       실행문1
#    else:
#       실행문2
# else:
#   실행문3


# ex) 4-8b 두개의 수를 입력받아 큰 수를 출력
# 같은 수 2개를 입력했을 때 처리하는 코드도 추가
# 또한, 음수 입력시 '양수만 입력하세요'라고 하고 종료
num = int(input('첫 번째 숫자입력 : '))
num2 = int(input('두 번째 숫자입력 : '))

if num > 0 and num > 0:
    if num > num2:
        result = f'두 수 중에 큰수는 {num}이고 작은 수는 {num2}입니다'
    elif num > num:
        result = f'두 수 중에 큰수는 {num2}이고 작은 수는 {num}입니다'
    else:
        result = f'입력한 두 수가 같습니다'
else:
    result = '양수만 입력하세요!'

print(result)

# ex) 4-10b 과목 점수에 대한 학점 처리
# 단, 입력한 점수가 100을 초과하면 '점수를 잘못 입력하셨습니다!'라고 출력하고 종료
jumsu = int(input('점수를 입력하세요 : '))

if 0 <= jumsu <= 100:
    if jumsu >= 90:
        result = 'A학점입니다'
    elif jumsu >= 80:
        result = 'B학점입니다'
    elif jumsu >= 70:
        result = 'C학점입니다'
    elif jumsu >= 60:
        result = 'D학점입니다'
    else:
        result = 'F학점입니다'
else:
    result = '점수를 잘못 입력하셨습니다!'

print(result)


# 문자열 비교
# ==, != : 문자열 내용과 생성된 메모리 위치 비교
# >, <, >=, <= : 문자열을 사전순(유니코드 순서)으로 비교
print('a' > 'A')            # a:97, A:65
print('*' < 'k')            # *:42, K:107
print('김' < '강')           # 김:44608, 강:44053
print('cskim' < 'CSKIM')    # c:99, C:67
print('John' < 'Joho')      # n:110, o:111
print('홍길덩' < '홍길딩')     # 덩:46020, 딩:46308

# 대소문자 구분없이 비교
print('cskim' < 'CSKIM'.lower())
print('cskim'.upper() < 'CSKIM')

# ex) 4-14 성별, 키, 몸무게를 입력받아
# 표준체중, 과체중, 비만체중 여부 판단
gender = input("성별 입력('M/m' 또는 'F/f'): ")
height = int(input('키 입력(cm) : '))
weight = float(input('몸무게 입력(kg) : '))

#처리
gender = gender.upper()     #성별을 대문자 변환
is_valid_gender = gender == 'F' or gender == 'M'

if is_valid_gender:
    # 표준 체중 계산
    height = height / 100  # 키(cm)를 m로 변환
    if gender == 'M':
        std_wght = height * height * 22
    elif gender == 'F':
        std_wght = height * height * 21
    # result = std_wght     #중간처리 결과 확인용1

    # 백분율 계산 (현재 체중이 표준체중의 몇%인지)
    # 몸무게 / 표준체중 * 100
    rate = (weight / std_wght) * 100
    # result = rate     #중간처리 결과 확인용2

    # 체중 상태 판별
    if rate < 100 :
        result = '표준 체중입니다!'
    elif rate < 119:
        result = '과체중입니다!'
    else:
        result = '비만 체중입니다!'
else:
    result = '성별 입력이 잘못 되었습니다'

#결과
print(result)


# match / case 문
# python 3.10부터 새롭게 추가된 조건 판별 구문
# if문은 조건식 결과가 참/거짓 여부에 따라 분기했었음
# 반면에, match/case문은 값이나 패턴에 따라 분기함
# match 변수:
# case 값1:
#    실행문1
# case 값2:
#    실행문2
# case 값3:
#    실행문3

# if vs match
# (복잡한)조건판단 : if
# 값/패턴비교 : match case

# ex) 4-10c 과목 점수에 대한 학점 처리
# 단, 입력한 점수가 100을 초과하면 '점수를 잘못 입력하셨습니다!'라고 출력하고 종료
# 학점 처리 부분을 match/case로 작성

jumsu = int(input('점수를 입력하세요 : '))

if 0 <= jumsu <= 100:
    # match jumsu:
    #     case 100 | 99 | 98 | 97 | 96 | 95 | 94 | 93 | 92 | 91 | 90:
    #         result = 'A학점입니다'
    #     case 89 | 88 | 87 | 86 | 85 | 84 | 83 | 82 | 81 | 80:
    #         result = 'B학점입니다'
    #     case 79 | 78 | 77 | 76 | 75 | 74 | 73 | 72 | 71 | 70:
    #         result = 'C학점입니다'
    #     case 69 | 68 | 67 | 66 | 65 | 64 | 63 | 62 | 61 | 60:
    #         result = 'D학점입니다'
    #     case _:
    #         result = 'F학점입니다'

    match jumsu // 10 :
        case 10 | 9:
            result = 'A학점입니다'
        case 8:
            result = 'B학점입니다'
        case 7:
            result = 'C학점입니다'
        case 6:
            result = 'D학점입니다'
        case _:
            result = 'F학점입니다'
else:
    result = '점수를 잘못 입력하셨습니다!'

print(result)

# ex) 1부터 10까지 총합을 구하는 코드 작성
sum = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
print(sum)
# 가우스 공식을 이용하면 빠르게 계산 가능

