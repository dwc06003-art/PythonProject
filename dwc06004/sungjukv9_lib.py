# 성적 처리프로그램 V9

import os
import sqlite3
import logging as log


menus = f'''
-------------------
성적처리 프로그램 V9
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

dbfile = 'sungjuk.db'


def sungjuk_logging():
    """로깅 설정을 초기화하는 함수"""
    log.basicConfig(
        filename = 'sungjuk9.log',
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
    sql = '''insert into sungjuk(name, kor, eng, mat, tot, avg, grd)
          values (?, ?, ?, ?, ?, ?, ?)'''

    if os.path.exists(dbfile):
        conn = sqlite3.connect(dbfile)
        print('add_sungjuk - DB 연결 성공!!')

        cursor = conn.cursor()
        cursor.execute(sql, (sj[0],sj[1],sj[2],sj[3],sj[4],sj[5],sj[6],))
        conn.commit()
        print('add_sungjuk - 성적 데이터 추가 완료!')

        conn.close()
    else:
        print('add_sungjuk - DB 연결 실패! - 파일이 존재하지 않아요!')

    log.info('add_sungjuk 호출됨!!')


def readall_sungjuk():
    """
    저장된 성적데이터 중 이름/국어/영어/수학만 출력

    :param sungjuks:
    :return:
    """
    result = ''
    sql = "select sjno, name, kor, eng, mat from sungjuk"

    if os.path.exists(dbfile):
        conn = sqlite3.connect(dbfile)
        print('readall_sungjuk - DB 연결 성공!!')

        cursor = conn.cursor()
        cursor.execute(sql)
        sungjuks = cursor.fetchall()
        conn.close()
    else:
        print('readall_sungjuk - DB 연결 실패! - 파일이 존재하지 않아요!')

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
    sql = "select * from sungjuk where sjno = ?"

    try:
        sjno = int(input('조회할 학생번호는? : '))

        if os.path.exists(dbfile):
            conn = sqlite3.connect(dbfile)
            print('readone_sungjuk - DB 연결 성공!!')

            cursor = conn.cursor()
            cursor.execute(sql, (sjno,))
            sj = cursor.fetchone()
            conn.close()
        else:
            print('readone_sungjuk - DB 연결 실패! - 파일이 존재하지 않아요!')

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
    sql1 = 'select * from sungjuk where sjno = ?'
    sql2 = '''update sungjuk set kor=?, eng=?, mat=?,
           tot=?, avg=?, grd=? where sjno=?'''
    try:
        sjno = int(input('수정할 학생번호는? : '))

        # 수정할 성적데이터를 성적테이블에서 읽어옴
        if os.path.exists(dbfile):
            conn = sqlite3.connect(dbfile)
            print('modify_sungjuk - DB 연결 성공!!')

            cursor = conn.cursor()
            cursor.execute(sql1, (sjno,))
            sj = cursor.fetchone()
            conn.close()
        else:
            print('modify_sungjuk - DB 연결 실패! - 파일이 존재하지 않아요!')

        if not sj:      # 수정할 성적데이터가 없다면
            print('수정할 데이터가 없어요!')
            return

        # 새로운 성적데이터를 입력받아 성적처리 한 후, 성적테이블에 적용
        kor = int(input(f'새로운 국어점수는? ({sj[2]}) :'))
        eng = int(input(f'새로운 국어점수는? ({sj[3]}) :'))
        math = int(input(f'새로운 국어점수는? ({sj[4]}) :'))

        sjone = compute_sungjuk(sj[1], kor, eng, math)

        if os.path.exists(dbfile):
            conn = sqlite3.connect(dbfile)
            print('modify_sungjuk - DB 연결 성공2!!')

            cursor = conn.cursor()
            cursor.execute(sql2, (kor,eng,math,sjone[4],sjone[5],sjone[6],sjno,))
            conn.commit()
            conn.close()
        else:
            print('modify_sungjuk - DB 연결 실패2! - 파일이 존재하지 않아요!')


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
    sql = "delete from sungjuk where sjno = ?"

    try:
        sjno = int(input('삭제할 학생 번호는? : '))

        if os.path.exists(dbfile):
            conn = sqlite3.connect(dbfile)
            print('remove_sungjuk - DB 연결 성공!!')

            cursor = conn.cursor()
            cursor.execute(sql, (sjno,))

            conn.commit()
            conn.close()

            print('성적 데이터가 삭제되었습니다!!')
            log.info('remove_sungjuk 호출됨!')

        else:
            print('remove_sungjuk - DB 연결 실패! - 파일이 존재하지 않아요!')



    except ValueError as ex:
        print('성적 삭제 조회시 숫자만 입력하세요')
        log.error(f'remove_sungjuk에서 오류발생! {type(ex)}')
