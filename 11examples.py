# 21
salary = int(input('연봉을 입력하세요(만원단위) : '))
isMarried = input('결혼여부를 입력하세요(y : 결혼, n : 미혼) : ').lower()
tax = 0
rate = 0

if isMarried == 'n':
    rate = 25
    if salary < 3000:
        rate = 10
elif isMarried == 'y':
    rate = 25
    if salary < 6000:
        rate = 10
else :
    print('결혼여부오류')

tax = salary * (rate / 100)
result = f'''
적용세율 : {rate}%
납부해야 할 세금은 {tax}만원 입니다.
'''
print(result)


# 23
import random

# 문자열 슬라이싱을 위해 생성한 난수는 문자형으로 변환
lotto = str (random.randint(123, 789))    #난수 생성
# 문자열 슬라이싱을 위해 문자형으로 입력받음
mykey = input('복권 숫자 3자리를 입력하세요 (예:123) : ')
#
prize = 0

# lotto = 357     # 난수로 생성한 3자리 숫자
# mykey = 357     # 사용자가 입력한 3자리 숫자

# num1 = lotto // 100
# num2 = (lotto % 100) // 10
# num3 = (lotto % 100) % 10

# key1 = mykey // 100
# key2 = (mykey % 100) // 10
# key3 = (mykey % 100) % 10

match = 0   #일치여부
if lotto[0] == mykey[0] or lotto[0] == mykey[1] or lotto[0] == mykey[2]:
    match += 1      # match = match + 1
if lotto[1] == mykey[0] or lotto[1] == mykey[1] or lotto[1] == mykey[2]:
    match += 1  # match = match + 1
if lotto[2] == mykey[0] or lotto[2] == mykey[1] or lotto[2] == mykey[2]:
    match += 1  # match = match + 1

if match == 3: prize = 1000000
elif match == 2: prize = 10000
elif match == 1: prize = 1000


result = f'''
당첨번호 : {lotto}
당신의 복권번호 : {mykey}
일치한 숫자 갯수 : {match}
당첨 금액 : {prize}원
'''


print(result)


# 26
import random

# 1~100 사이 임의의 난수 생성
number = random.randint(1,100)
# 사용자로부터 값을 하나 입력 받음
mynum = int(input('1~100사이 숫자를 하나 입력하세요 : '))

result = '빙고! 숫자를 맞췄습니다!!'
if number > mynum: result = '추측한 숫자가 작아요'
elif number < mynum: result = '추측한 숫자가 커요'

print(f'{number} : {result}')

# 31
cardnum = input('6자리 카드번호를 입력하세요 : ')
# cardnum = '999999'
cartdtype = '식별안됨'
cardbank = '식별안됨'

if len (cardnum) == 6:
    if cardnum[:2] == '35':
        cardtype = 'JCB카드'
        if cardnum[2:] == '6317': cardbank = 'NH농협카드'
        elif cardnum[2:] == '6901': cardbank = '신한카드'
        elif cardnum[2:] == '6912': cardbank = 'KB국민카드'
        else: cardbank = '은행정보는 등록되지 않았습니다'
    elif cardnum[0] == '4':
        cardtype = '비자카드'
        if cardnum[1:] == '04825': cardbank = '비씨카드'
        elif cardnum[1:] == '38676': cardbank = '신한카드'
        elif cardnum[1:] == '57973': cardbank = '국민은행'
        else: cardbank = '은행정보는 등록되지 않았습니다'
    elif cardnum[0] == '5':
        cardtype = '마스터카드'
        if cardnum[1:] == '15594': cardbank = '신한카드'
        elif cardnum[1:] == '24353': cardbank = '외환카드'
        elif cardnum[1:] == '40926': cardbank = '국민은행'
        else : cardbank = '은행정보는 등록되지 않았습니다'
    else: cardbank = '올바른 카드번호가 아닙니다'
else:
    cardtype = '카드번호는 6자리여야 합니다'

result= f'카드종류 및 은행 : {cardtype} - {cardbank}'

print(result)

# 32
# jumin = input('주민번호를 입력하세요 (xxxxxx-yyyyyyy): ')
jumin = '012346-1234567'
sum = 0

# a, b
sum += int(jumin[0]) * 2
sum += int(jumin[1]) * 3
sum += int(jumin[2]) * 4
sum += int(jumin[3]) * 5
sum += int(jumin[4]) * 6
sum += int(jumin[5]) * 7
sum += int(jumin[7]) * 8
sum += int(jumin[8]) * 9
sum += int(jumin[9]) * 2
sum += int(jumin[10]) * 3
sum += int(jumin[11]) * 4
sum += int(jumin[12]) * 5

print(sum)

# c
remainder = sum % 11
print(remainder)
# d
checker = 11 - remainder
print(checker, str(checker)[-1] == jumin[13])


