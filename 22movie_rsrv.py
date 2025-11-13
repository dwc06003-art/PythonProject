#

# menus = f'''
# 영화관 좌석 예매
# -------------------
# 1. 좌석 선택
# 2. 현재 좌석 현황
# * 프로그램 종료는 quit을 입력해주세요
# 보기를 선택해주세요 : '''
# seat = [
#     ['A', 'O', 'O', 'O','O','O'],
#     ['B', 'O', 'O', 'O','O','O'],
#     ['C', 'O', 'O', 'O','O','O'],
#     ['D', 'O', 'O', 'O','O','O'],
#     ['E', 'O', 'O', 'O','O','O']
# ]
#
# while True:
#     sel = input(menus)
#     match sel:
#         case '1':
#             x = input('몇 번 좌석을 예약하시겠어요?(행 a ~ e) : ').lower()
#             y = int(input('몇 번 좌석을 예약하시겠어요?(열 1 ~ 5) : '))
#             match x:
#                 case 'a':
#                     if seat[0][y] == 'X':
#                         print('이미 예약된 좌석입니다.')
#                     else:
#                         seat[0][y] = 'X'
#                         print(f'{x}{y}예약')
#                 case 'b':
#                     if seat[1][y] == 'X':
#                         print('이미 예약된 좌석입니다.')
#                     else:
#                         seat[1][y] = 'X'
#                         print(f'{x}{y}예약')
#                 case 'c':
#                     if seat[2][y] == 'X':
#                         print('이미 예약된 좌석입니다.')
#                     else:
#                         seat[2][y] = 'X'
#                         print(f'{x}{y}예약')
#                 case 'd':
#                     if seat[3][y] == 'X':
#                         print('이미 예약된 좌석입니다.')
#                     else:
#                         seat[3][y] = 'X'
#                         print(f'{x}{y}예약')
#                 case 'e':
#                     if seat[4][y] == 'X':
#                         print('이미 예약된 좌석입니다.')
#                     else:
#                         seat[4][y] = 'X'
#                         print(f'{x}{y}예약')
#                 case _:
#                     print('잘못입력하셨습니다')
#         case '2':
#             for k in range(5):
#                 for l in range(6):
#                      print(seat[k][l], end=' ')
#                 print()
#         case 'quit':
#             print('이용해주셔서 감사합니다!')
#             break

# 영화관 좌석 예약 프로그램
# 5 행 5열(총 25석) 영화관좌석
# 각좌석은 처음에 모두 빈 자리 ('O')로 표시
# 이미 예약된 좌석은 예약 불가 메세지를 출력

# 좌석 초기화
seats = []

for i in range(5):
    row = []
    for j in range(5):
        row.append('O')
    seats.append(row)

# 좌석 현황 출력 후
result = '   1  2  3  4  5\n'

for j in range(5):
    result += f'{chr(65 + j):3s}'
    for i in range(5):
        result += f'{seats[j][i]:3s}'
    result +='\n'
print(result)

# 예약 여부 입력 받음
rsrv_row = input('좌석을 예약하시겠어요? 행(A~E) : ').upper()
rsrv_col = input('좌석을 예약하시겠어요? 열(1~5) : ')

# 좌석 예약 처리
posx = ord(rsrv_row) - 65
posy = int(rsrv_col) - 1
seats[posx][posy] = 'X'

# 예약 확인
result = '   1  2  3  4  5\n'

for j in range(5):
    result += f'{chr(65 + j):3s}'
    for i in range(5):
        result += f'{seats[j][i]:3s}'
    result +='\n'
print(f'\n{result}')

# 처리 완료 메세지 출력
print(f'{rsrv_row}{rsrv_col} 좌석이 예약되었습니다!')
