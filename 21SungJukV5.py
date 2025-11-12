# 성적 처리프로그램 V5
# 이름, 국어, 영어 수학, 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 성적처리의 CRUD를 메뉴식으로 구현
# 성적 데이터를 시퀀스 자료형에 저장
# sungjuks = [
#     ['혜교', 99, 98, 297, 99.99, 'A'],
#     ['지연', 33, 44, 55, 197, 77.82, 'C'],
#     ['수지', 77, 88, 99, 235, 85.99, 'B']
# ]

menus = f'''
-------------------
성적처리 프로그램 V4
-------------------
1. 성적데이터 입력
2. 성적데이터 조회
3. 성적데이터 상세조회
4. 성적데이터 수정
5. 성적데이터 삭제
0. 프로그램 종료
-------------------
작업을 선택하세요 : '''

header = '''
이름      국어  영어  수학  총점  평균 학점
------------------------------------
'''

sungjuks = []   #성적데이터 저장용 변수

while True:
    job = input(menus)
    match job:
        case '1':
            name = input(f'학생 정보 입력 \n이름을 입력하세요 : ')
            kor = int(input(f'국어 점수를 입력하세요 : '))
            eng = int(input(f'영어 점수를 입력하세요 : '))
            math = int(input(f'수학 점수를 입력하세요 : '))

            # 성적처리
            tot = kor + eng + math
            avg = tot / 3
            grd = ('A' if (avg >= 90) else
                   'B' if (avg >= 80) else
                   'C' if (avg >= 70) else
                   'D' if (avg >= 60) else 'F')

            # 입력 받아 처리한 성적데이터를 리스트로 만들어
            sj = [name, kor, eng, math, tot, avg, grd]
            # sungjuks 라는 리스트에 저장
            sungjuks.append(sj)

            print('입력한 데이터에 대해 성적처리가 완료되었습니다!')

        case '2':
            result = ''
            for name,kor,eng,math,tot,avg,grd in sungjuks:
                result += f'{name:5s} {kor:4d} {eng:4d} {math:4d}'\
                     f' {tot:4d}  {avg:.2f} {grd:3s}\n'

                print(f'{header}{result}')

        case '3':print('성적데이터 상세조회를 진행합니다...')
        case '4':print('성적데이터 수정을 진행합니다...')
        case '5':print('성적데이터 삭제를 진행합니다...')
        case '0':
            print('성적프로그램을 종료합니다...')
            break
        case _: print('번호를 잘못입력하셨습니다!')
