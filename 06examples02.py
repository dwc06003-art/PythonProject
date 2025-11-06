# 8
# 아스키코드표
print('a', 3 + 4.5 * 2 + 27 / 8)
print('b', True or False and 3 < 4 or not(5 == 7))
print('c', True or (3 < 5 and 6 >= 2 ))
# print('d', not True > 'A' )           # 잘못된 표현식
# print('e', 7 % 4 + 3 - 2 / 6 * 'Z')   # 잘못된 표현식
# print('f', 'D' + 1 + 'M' % 2 /3)      # 잘못된 표현식
print('g', 5.0 / 3 + 3 / 3)
print('h', 53 % 21 < 45 / 18)
print('i', (4 < 6) or True and False or False and (2 > 3))
print('j', 7 - (3 + 8 * 6 + 3) - (2 + 5 * 2))

# 9
print ('a', "May 13, 1988 fell on day number")
print('b', ((13 + (13 * 3 - 1) / 5 + 1988 % 100 + 1988 % 100 / 4
            + 1988 / 400 - 2 * (1988 / 100)) % 7 + 7) % 7)
# zeller의 공식 : 1998년 3월 13일의 요일 계산
# q : 일, m : 월, K : 연도(뒷두자리), J : 연도(앞두자리)
# h = (q + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) + 5 * 7) % 7
print()

# 22 - 윤년
# 1년은 365일이지만, 실제는 365.24일
# 이러한 오차를 보정하기 위해 4년에 한번씩 2월 29일까지 둠(평년에는 28일)
# 판정기준
# a : 현재 연도가 4로 나눠 떨어지지만, 100으로 나눠 떨어지지 않음
# b : 그중에서도 400으로 나눠떨어지면
# 2024, 2000, 2100 : 윤년
year = 2020
result = '윤년' if ((year % 4 == 0) and (year % 100 != 0)
                  or (year % 400 == 0)) else '평년'
print(result)

# 파이썬 표준라이브러리를 사용하면 편하게 코드 작성 가능
import calendar

print(calendar.isleap(2024))
print(calendar.isleap(2025))

# 35 - 거스름돈 계산
# 지불할 금액 : 32100
# 지불한 금액 : 50000
# 거스름돈 : 17900
# product = 32100
# pay = 50000
# charge = pay - product
# print(f'물건가격 : {product}, 지불금액 : {pay}, 거스름돈 : {charge}')

# n50000 = int(charge / 50000)
# print('50000원', int(n50000), '개')
# charge = charge - (50000 * n50000)
#
# n10000 = int(charge / 10000)
# print('10000원', int(n10000), '개')
# charge = charge - (10000 * n10000)
#
# n5000 = int(charge / 5000)
# print('5000원', int(n5000), '개')
# charge = charge - (5000 * n5000)
#
# n1000 = int(charge / 1000)
# print('1000원', int(n1000), '개')
# charge = charge - (1000 * n1000)
#
# n500 = int(charge / 500)
# print('500원', int(n500), '개')
# charge = charge - (500 * n500)
#
# n100 = int(charge / 100)
# print('100원', int(n100), '개')
# charge = charge - (100 * n100)
#
# n50 = int(charge / 50)
# print('50원', int(n50), '개')
# charge = charge - (50 * n50)
#
# n10 = int(charge / 10)
# print('10원', int(n10), '개')
# charge = charge - (10 * n10)

# --------

# 입력
product = int(input('물건 가격을 입력하세요 : '))
pay = int(input('손님이 지불한 금액을 입력하세요 : '))

# 잔돈 계산
charge = pay - product

n50000 = charge // 50000
charge = charge % 50000

n10000 = charge // 10000
charge = charge % 10000

n5000 = charge // 5000
charge = charge % 5000

n1000 = charge // 1000
charge = charge % 1000

n500 = charge // 500
charge = charge % 500

n100 = charge // 100
charge = charge % 100

n50 = charge // 50
charge = charge % 50

n10 = charge // 10
charge = charge % 10

# 계산 결과 출력
# print(f'거스름돈 총액 : {pay - product} 원')
# print(f'50000원 : {n50000} 개')
# print(f'10000원 : {n10000} 개')
# print(f'5000원 : {n5000} 개')
# print(f'1000원 : {n1000} 개')
# print(f'500원 : {n500} 개')
# print(f'100원 : {n100} 개')
# print(f'50원 : {n50} 개')
# print(f'10원 : {n10} 개')

pfmt = f'''
거스름돈 총액 : {pay - product} 원
50000원 : {n50000} 개
10000원 : {n10000} 개
5000원 : {n5000} 개
1000원 : {n1000} 개
500원 : {n500} 개
100원 : {n100} 개
50원 : {n50} 개
10원 : {n10} 개
'''
print(pfmt)