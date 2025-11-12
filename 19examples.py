# 21 - 반복추가
while True:
    salary = int(input('연봉을 입력하세요(만원단위) : '))
    isMarried = input('결혼여부를 입력하세요(y : 결혼, n : 미혼) : ').lower()
    tax = 0
    rate = 0

    match isMarried:
        case 'n':
            rate = 25
            if salary < 3000: rate = 10
        case 'y':
            rate = 25
            if salary < 3000: rate = 10
        case _: print('결혼여부 오류!!')

    tax = salary * (rate / 100)
    result = f'''
    적용세율 : {rate}%
    납부해야 할 세금은 {tax}만원 입니다.
    '''
    print(result)
    cont = input('계속하시겠습니까? (y/n) :').lower()
    if cont == 'n': break

# 23 - 중첩
import random

lotto = str (random.randint(123, 789))    #난수 생성
mykey = input('복권 숫자 3자리를 입력하세요 (예:123) : ')

prize = 0
match = 0

for i in range(3):
    for j in range(3):
        if lotto[i] == mykey[j]: match += 1

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

# 26 - 반복 추가2
import random

number = random.randint(1,100)

while True:
    mynum = int(input('1~100사이 숫자를 하나 입력하세요 : '))
    result = '빙고! 숫자를 맞췄습니다!!'
    if number > mynum: result = '추측한 숫자가 작아요'
    elif number < mynum: result = '추측한 숫자가 커요'
    elif number == mynum: break
    print(result)

print(f'{number} : {result}')

# 30 - 중첩
result = f'''
          Multiplication Table
      1   2   3   4   5   6   7   8   9
---------------------------------------
'''

for i in range(1, 9+1):
    result += f'{i} | '
    for j in range(1, 9+1):
        result += f'{i * j:3d} '
    result += '\n'

print(result)

# 31 - match ~ case로 변경
cardnum = input('6자리 카드번호를 입력하세요 : ')
cartdtype = '식별안됨'
cardbank = '식별안됨'

if len (cardnum) == 6:
    match cardnum[0]:
        case '3':
            cardtype = 'JCB카드'
            match cardnum[1:]:
                case '56317': cardbank = 'NH농협카드'
                case '56901': cardbank = '신한카드'
                case '56912': cardbank = 'KB국민카드'
                case _: cardbank = '은행정보는 등록되지 않았습니다'
        case '4':
            cardtype = '비자카드'
            match cardnum[1:]:
                case '04825': cardbank = '비씨카드'
                case '38676': cardbank = '신한카드'
                case '57973': cardbank = '국민은행'
                case _: cardbank = '은행정보는 등록되지 않았습니다'
        case '5':
            cardtype = '마스터카드'
            match cardnum[1:]:
                case '15594': cardbank = '신한카드'
                case '24353': cardbank = '외환카드'
                case '40926': cardbank = '국민은행'
                case _: cardbank = '은행정보는 등록되지 않았습니다'
else:
    cardtype = '카드번호는 6자리여야 합니다'

result= f'카드종류 및 은행 : {cardtype} - {cardbank}'

print(result)