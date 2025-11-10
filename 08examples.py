#10
print('a.', True and False and True or True)
print('b.', True or True and True and False)
print('c.', (True and False) or (True and not False) or (False and not False))
print('d.', (2 < 3) or (5 > 2) and not (4 == 4) or 9 != 4)
print('e.', 6 == 9 or 5 < 6 and 8 < 4 or 4 > 3)

#11
print('a.', 27 / 13 + 4)
print('b.', 27 / 13 + 4.0)
print('c.', 42.7 % 3 + 18)
print('d.', (3, 4) and 5 / 8)
print('e.', 23 / 5 + 23 / 5.0)
# print('f.', 2.0 + 'a')
# print('g.', 2 + 'a')
print('h.', 'a' + 'b')
# print('i.', 'a' / 'b')
print('j.', 'a' and not 'b')
# print('k.', (double) 'a' / 'b'

#12
n = int(3.9)
#print("n ==" + n)

#14
# print("2 + 2 =" + (2 + 2))
# print("2 + 2 =" + 2 + 2)

#24
dan = int(input('출력할 구구단 단수를 입력하세요 (1-9) : '))

if 1 <= dan <=9:
    result = f'''
    === {dan}단 ===
    {dan} * 1 = {dan * 1}
    {dan} * 2 = {dan * 2}
    {dan} * 3 = {dan * 3}
    {dan} * 4 = {dan * 4}
    {dan} * 5 = {dan * 5}
    {dan} * 6 = {dan * 6}
    {dan} * 7 = {dan * 7}
    {dan} * 8 = {dan * 8}
    {dan} * 9 = {dan * 9}
'''
else:
    result = '잘못입력하셨습니다!'

print(result)

#25
# 문자 입력 - input() 이용
# ASCII 코드표 - A: 65, a: 97 => 변환시 -32 적용
# 문자를 코드값으로  변환 : ord
# 코드값를 문자로  변환 : chr
# 소문자 범위 체크 : a97 ~ z122

char = input('소문자를 하나 입력하세요 (a-z): ')

# 입력한 문자가 소문자인지 확인
if len(char) == 1 and 'a' <= char <= 'z':
    # result = char.upper()
    result = chr(ord(char) - 32)


else:
    result = '잘못 입력하셨습니다!'

print(result)

#30
result = f'''
        Multiplication Table
     1   2   3   4   5   6   7   8   9
--------------------------------------
1 |  1   2   3   4   5   6   7   8   9
2 |  2   4   6   8  10  12  14  16  18
3 |  3   6   9  12  15  18  21  24  27
4 |  4   8  12  16  20  24  28  32  36 
5 |  5  10  15  20  25  30  35  40  45
6 |  6  12  18  24  30  36  42  48  54
7 |  7  14  21  28  35  42  49  56  63
8 |  8  16  24  32  40  48  56  64  72
9 |  9  18  27  36  45  54  63  72  81   
'''


print(result)


#36 - 시간계산
# 하루는 86400초, 한시간은 3600초, 일분은 60초
day_sec = 86400
hour_sec = 3600
min_sec = 60


result = f'''
{1234567890:,}초는 {1234567890 // day_sec:,}일 입니다.
{12345:,}초는 {12345 // hour_sec:,}시간입니다.
{67890:,}초는 {67890 // min_sec:,}분입니다.
'''

print(result)