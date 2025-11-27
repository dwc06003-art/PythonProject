# 성적 처리프로그램 V10용 모듈
# sungjukv10 -> sungjukv10_lib -> sungjukv10_dao

import logging as log
from dwc06004.sungjukv10_dao import manuplate_query
from dwc06004.sungjukv10_dao import retrieve_query
from dwc06004.sungjukv10_dao import insert_sungjuk_sql
from dwc06004.sungjukv10_dao import update_sungjuk_sql
from dwc06004.sungjukv10_dao import delete_sungjuk_sql
from dwc06004.sungjukv10_dao import select_sungjuk_sql
from dwc06004.sungjukv10_dao import selectone_sungjuk_sql


menus = f'''
-------------------
성적처리 프로그램 V10
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




def sungjuk_logging():
    """로깅 설정을 초기화하는 함수"""
    log.basicConfig(
        filename = 'sungjuk10.log',
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


def add_sungjuk(sj):
    """
    처리한 성적데이터를 리스트에 추가

    :return:
    """

    params = (sj[0],sj[1],sj[2],sj[3],sj[4],sj[5],sj[6],)
    manuplate_query(insert_sungjuk_sql, params)
    print('add_sungjuk - 성적 데이터 추가 완료!')

    log.info('add_sungjuk 호출됨!!')


def readall_sungjuk():
    """
    저장된 성적데이터 중 이름/국어/영어/수학만 출력

    :param sungjuks:
    :return:
    """
    result = ''

    params = ()
    sungjuks = retrieve_query(select_sungjuk_sql, params, 'all')

    for sj in sungjuks:
        result += f'{sj[0]:2d} {sj[1]:5s} {sj[2]:4d} {sj[3]:4d} {sj[4]:4d}\n'

    print(f'{header1}{result}')
    log.info('readall_sungjuk 호출됨!')


def readone_sungjuk():
    """
    이름으로 성적데이터를 조회해서 모두 출력

    :param sungjuks:
    :return:
    """
    result = ''

    try:
        sjno = int(input('조회할 학생번호는? : '))

        params = (sjno,)
        sj = retrieve_query(selectone_sungjuk_sql, params, 'one')

        if sj:      # 성적데이터 조회되었다면
            result += f'{sj[0]:2d} {sj[1]:5s} {sj[2]:4d} {sj[3]:4d} {sj[4]:4d}' \
                      f'{sj[5]:5d}  {sj[6]:.2f} {sj[7]:3s} {sj[8]}\n'


        print(f'{header2}{result}')
        log.info('readone_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 상세 조회시 숫자만 입력하세요')
        log.error(f'readone_sungjuk에서 오류발생! {type(ex)}')


def modify_sungjuk():
    """
    기존 성적데이터를 새로운 성적데이터로 수정하는 함수

    :param sungjuks:
    :return:
    """
    result = '해당 학생번호가 존재하지 않아요!!'

    try:
        sjno = int(input('수정할 학생번호는? : '))

        params = (sjno,)
        sj = retrieve_query(selectone_sungjuk_sql, params, 'one')

        if not sj:      # 수정할 성적데이터가 없다면
            print('수정할 데이터가 없어요!')
            return

        # 새로운 성적데이터를 입력받아 성적처리 한 후, 성적테이블에 적용
        kor = int(input(f'새로운 국어점수는? ({sj[2]}) :'))
        eng = int(input(f'새로운 국어점수는? ({sj[3]}) :'))
        math = int(input(f'새로운 국어점수는? ({sj[4]}) :'))

        sjone = compute_sungjuk(sj[1], kor, eng, math)

        params = (kor,eng,math,sjone[4],sjone[5],sjone[6],sjno,)
        manuplate_query(update_sungjuk_sql, params)

        result = '성적수정이 완료되었습니다'
        print(result)
        log.info('modify_sungjuk 호출됨!')
    except ValueError as ex:
        print('성적 수정시 숫자만 입력하세요')
        log.error(f'modify_sungjuk에서 오류발생! {type(ex)}')


def remove_sungjuk():
    """
    특정 학생의 성적데이터를 삭제하는 함수

    :param sungjuks:
    :return:
    """

    result = '해당 학생번호가 존재하지 않아요!!'
    try:
        sjno = int(input('삭제할 학생 번호는? : '))

        params = (sjno,)
        manuplate_query(delete_sungjuk_sql, params)

        print('성적 데이터가 삭제되었습니다!!')
        log.info('remove_sungjuk 호출됨!')

    except ValueError as ex:
        print('성적 삭제 조회시 숫자만 입력하세요')
        log.error(f'remove_sungjuk에서 오류발생! {type(ex)}')
