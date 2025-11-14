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

header1 = '''
이름      국어  영어  수학
-----------------------
'''

header2 = '''
이름      국어  영어  수학  총점  평균 학점
------------------------------------
'''


def input_sungjuk():
    """
    성적 데이터를 입력받는 함수

    :return:
    """
    name = input(f'학생 정보 입력 \n이름을 입력하세요 : ')
    kor = int(input(f'국어 점수를 입력하세요 : '))
    eng = int(input(f'영어 점수를 입력하세요 : '))
    math = int(input(f'수학 점수를 입력하세요 : '))

    return name, kor, eng, math


def compute_sungjuk(name, kor, eng, math):
    """
    성적 데이터에 대한 총점,평균,학점 처리

    :return:
    """
    tot = kor + eng + math
    avg = tot / 3
    grd = ('A' if (avg >= 90) else
           'B' if (avg >= 80) else
           'C' if (avg >= 70) else
           'D' if (avg >= 60) else 'F')

    return [name, kor, eng, math, tot, avg, grd]


def add_sungjuk(sj, sungjuks):
    """
    처리한 성적데이터를 리스트에 추가

    :return:
    """
    sungjuks.append(sj)


def readall_sungjuk(sungjuks):
    """
    저장된 성적데이터 중 이름/국어/영어/수학만 출력

    :param sungjuks:
    :return:
    """
    result = ''
    for name, kor, eng, math, tot, avg, grd in sungjuks:
        result += f'{name:5s} {kor:4d} {eng:4d} {math:4d}\n'

    print(f'{header1}{result}')


def readone_sungjuk(sungjuks):
    """
    이름으로 성적데이터를 조회해서 모두 출력

    :param sungjuks:
    :return:
    """
    result = ''

    namekey = input('조회할 학생이름은? : ')

    for name, kor, eng, math, tot, avg, grd in sungjuks:
        if namekey == name:
            result += f'{name:5s} {kor:4d} {eng:4d} {math:4d}' \
                      f'{tot:5d}  {avg:.2f} {grd:3s}\n'

    print(f'{header2}{result}')


def modify_sungjuk(sungjuks):
    """
    기존 성적데이터를 새로운 성적데이터로 수정하는 함수

    :param sungjuks:
    :return:
    """
    result = '해당 학생이 존재하지 않아요!!'
    namekey = input('수정할 학생이름은? : ')

    # 수정할 학생이 존재하는지 확인
    # sungjuks[i]는 개별 성적데이터를 가리키는 포인터 pointer
    # sungjuks[i] = sjone 라는 코드를 이용해서
    # 따라서, compute_sungjuk 함수에 의해 새롭게 생성된 sj객체로 완전히 교체함
    # 즉, sungjuks[i]는 툭정 학생의 성적데이터를 가리키는 인덱스
    # sungjuks[i][j]는 학생 성적데이터의 특정요소를 가리키는 인덱스
    for i in range(len(sungjuks)):
        if namekey == sungjuks[i][0]:
            # 수정작업 진행
            kor = int(input(f'새로운 국어점수는? ({sungjuks[i][1]}) :'))
            eng = int(input(f'새로운 국어점수는? ({sungjuks[i][2]}) :'))
            math = int(input(f'새로운 국어점수는? ({sungjuks[i][3]}) :'))

            sjone = compute_sungjuk(sungjuks[i][0], kor, eng, math)
            sungjuks[i] = sjone


            result = '성적수정이 완료되었습니다'
            break

    print(result)

def remove_sungjuk(sungjuks):
    """
    특정 학생의 성적데이터를 삭제하는 함수

    :param sungjuks:
    :return:
    """

    result = '해당 학생이 존재하지 않아요!!'
    namekey = input('삭제할 학생이름은? : ')

    for i in range(len(sungjuks)):
        if namekey == sungjuks[i][0]:
            sungjuks.pop(i)
            result = '성적 데이터가 삭제되었습니다!!'
            break

    print(result)