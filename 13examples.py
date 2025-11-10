# 23 복권 - 반복문으로 재작성
# import random
#
# lotto = str (random.randint(123, 789))    #난수 생성
# mykey = input('복권 숫자 3자리를 입력하세요 (예:123) : ')
#
# prize = 0
# match = 0
#
# # 개선된 코드 1
# # for i in range(0, 3):
# #     if lotto[i] == mykey[0] or lotto[i] == mykey[1] or lotto[i] == mykey[2]:
# #         match += 1
#
# # 개선된 코드 2
# for i in range(0, 3):
#     if lotto[i] == mykey[0]: match += 1
#     if lotto[i] == mykey[1]: match += 1
#     if lotto[i] == mykey[2]: match += 1
#
# if match == 3: prize = 1000000
# elif match == 2: prize = 10000
# elif match == 1: prize = 1000
#
#
# result = f'''
# 당첨번호 : {lotto}
# 당신의 복권번호 : {mykey}
# 일치한 숫자 갯수 : {match}
# 당첨 금액 : {prize}원
# '''
#
# print(result)

# 24 구구단 - 반복문으로 재작성
# dan = int(input('출력할 구구단 단수를 입력하세요 (1-9) : '))
#
# if 1 <= dan <=9:
#     result = f'==={dan}단===\n'
#     for i in range(1, 10):
#         result += f'{dan} * {i} = {dan * i}\n'
# else:
#     result = '잘못입력하셨습니다!'
#
# print(result)

# 26 숫자 맞추기 - 반복문 추가
# 반복문에서 반복 중단하려면 break 사용
# import random
#
# number = random.randint(1,100)
# result = ''
#
# for _ in range(1, 25+1):
#     mynum = int(input('1~100사이 숫자를 하나 입력하세요 : '))
#     result = '빙고! 숫자를 맞췄습니다!!'
#     if number > mynum: result = '추측한 숫자가 작아요'
#     elif number < mynum: result = '추측한 숫자가 커요'
#     elif number == mynum: break     # 숫자를 맞추면 반복에서 중단
#     print(result)
#
# print(f'{number} : {result}')

# 30 구구단 테이블 - 반복문으로 재작성
result = f'''
          Multiplication Table
      1   2   3   4   5   6   7   8   9
---------------------------------------
'''

for i in range(1, 9+1):
    result += f'{i} | {i*1:3d} {i*2:3d} {i*3:3d} {i*4:3d} {i*5:3d} {i*6:3d} {i*7:3d} {i*8:3d} {i*9:3d}\n'


print(result)


# 32 주민번호 검사 - 반복문 재작성
jumin = '123456-1234567'
sum = 0

# a, b
wght = 2
for i in range(0, 5+1):
    sum += int(jumin[i]) * (wght + i)

for i in range(7, 8+1):
    sum += int(jumin[i]) * (wght + i - 1)

for i in range(9, 12+1):
    sum += int(jumin[i]) * (wght + (i - 9))

print(sum)

# c,d
checker = 11 - (sum % 11)
print(checker, str(checker)[-1] == jumin[13])
