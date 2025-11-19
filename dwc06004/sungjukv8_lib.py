# 성적 처리프로그램 V8용 모듈

import csv
import logging as log

counts = 0  # 학생번호 부여용

menus = f'''
-------------------
성적처리 프로그램 V8
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
번호 이름      국어  영어  수학
---------------------------
'''

header2 = '''
번호 이름      국어  영어  수학  총점  평균 학점
-----------------------------------------
'''

fname = 'sungjuk.csv'


def sungjuk_logging():
    """로깅 설정을 초기화하는 함수"""
    log.basicConfig(
        filename = 'sungjuk8.log',
        level = log.INFO, encoding = 'utf-8',
        format = '%(asctime)s %(levelname)s --- %(message)s'
    )


def input_sungjuk():
    """
    성적 데이터를 입력받는 함수

    :return:
    """

    log.info('input_sungjuk 호출됨!')
    try:
        name = input(f'학생 정보 입력 \n이름을 입력하세요 : ')
        kor = int(input(f'국어 점수를 입력하세요 : '))
        eng = int(input(f'영어 점수를 입력하세요 : '))
        math = int(input(f'수학 점수를 입력하세요 : '))
    except ValueError:
        print('점수는 숫자만 입력가능합니다!')
        log.error('점수는 숫자만 입력가능합니다!')
        name, kor, eng, math = '0',0,0,0

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
    log.info('compute_sungjuk 호출됨!')

    return [name, kor, eng, math, tot, avg, grd]


def add_sungjuk(sj, sungjuks):
    """
    처리한 성적데이터를 리스트에 추가

    :return:
    """
    global counts
    counts += 1
    sj.insert(0, counts)
    sungjuks.append(sj)
    log.info('add_sungjuk 호출됨!!')


def readall_sungjuk(sungjuks):
    """
    저장된 성적데이터 중 이름/국어/영어/수학만 출력

    :param sungjuks:
    :return:
    """
    result = ''
    for sj in sungjuks:
        result += f'{sj[0]:2d} {sj[1]:5s} {sj[2]:4d} {sj[3]:4d} {sj[4]:4d}\n'

    print(f'{header1}{result}')
    log.info('readall_sungjuk 호출됨!')


def readone_sungjuk(sungjuks):
    """
    이름으로 성적데이터를 조회해서 모두 출력

    :param sungjuks:
    :return:
    """
    result = ''
    try:
        sjnokey = int(input('조회할 학생번호는? : '))

        for sj in sungjuks:
            if sjnokey == sj[0]:
                result += f'{sj[0]:2d} {sj[1]:5s} {sj[2]:4d} {sj[3]:4d} {sj[4]:4d}' \
                          f'{sj[5]:5d}  {sj[6]:.2f} {sj[7]:3s}\n'

        print(f'{header2}{result}')
        log.info('readone_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 상세 조회시 숫자만 입력하세요')
        log.error(f'readone_sungjuk에서 오류발생! {type(ex)}')


def modify_sungjuk(sungjuks):
    """
    기존 성적데이터를 새로운 성적데이터로 수정하는 함수

    :param sungjuks:
    :return:
    """
    result = '해당 학생번호가 존재하지 않아요!!'

    try:
        sjno = int(input('수정할 학생번호는? : '))

        for i in range(len(sungjuks)):
            if sjno == sungjuks[i][0]:
                # 수정작업 진행
                kor = int(input(f'새로운 국어점수는? ({sungjuks[i][2]}) :'))
                eng = int(input(f'새로운 국어점수는? ({sungjuks[i][3]}) :'))
                math = int(input(f'새로운 국어점수는? ({sungjuks[i][4]}) :'))

                sjone = compute_sungjuk(sungjuks[i][1], kor, eng, math)
                sjone.insert(0, sjno)
                sungjuks[i] = sjone


                result = '성적수정이 완료되었습니다'
                break

        print(result)
        log.info('modify_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 수정시 숫자만 입력하세요')
        log.error(f'modify_sungjuk에서 오류발생! {type(ex)}')


def remove_sungjuk(sungjuks):
    """
    특정 학생의 성적데이터를 삭제하는 함수

    :param sungjuks:
    :return:
    """

    result = '해당 학생번호가 존재하지 않아요!!'

    try:
        sjno = int(input('삭제할 학생 번호는? : '))

        for i in range(len(sungjuks)):
            if sjno == sungjuks[i][0]:
                sungjuks.pop(i)
                result = '성적 데이터가 삭제되었습니다!!'
                break

        print(result)
        log.info('remove_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 삭제 조회시 숫자만 입력하세요')
        log.error(f'remove_sungjuk에서 오류발생! {type(ex)}')


def load_sungjuk():
    """
    sungjuk.csv파일의 내용을 읽어서 리스트 변수에 저장

    :return:
    """
    sungjuks = []

    global counts

    log.info('load_sungjuk 호출됨!')
    try:
        with open(fname, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for items in reader:
                # print(f'items의 항목수 : {len(items)}\n')
                # 문자열로 저장된 성적데이터를 원래 자료형식에 맞게 변환작업 추가
                counts = int(items[0])       # 학생번호 설정
                sj = [int(items[0]), items[1], int(items[2]), int(items[3]), int(items[4]),
                     int(items[5]), float(items[6]), items[7]]
                sungjuks.append(sj)
            log.info('성적 데이터가 성공적으로 초기화되었습니다!!')
    except FileNotFoundError as ex:
        #print('sungjuk.csv 파일이 존재하지 않아요!!')
        log.error('sungjuk.csv 파일이 존재하지 않아요!!')
        pass
    return sungjuks


def write_sungjuk(sungjuks):
    try:
        with open(fname, 'w', encoding='utf-8') as f:
            for sj in sungjuks:
                row = (f'{sj[0]},{sj[1]},{sj[2]},{sj[3]},'
                       f'{sj[4]},{sj[5]},{sj[6]},{sj[7]}\n')
                f.write(row)
        log.info('write_sungjuk 호출됨!!')
    except Exception as ex:
        print('성적 데이터 저장시 오류 발생!! - 관리자에게 문의하세요!')
        log.error(f'write_sungjuk에서 오류발생!! {type(ex)}')