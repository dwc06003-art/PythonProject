# sqlite3 기반 성적처리 프로그램 모듈

import os
import sqlite3

# sql 변수정의
dbfile = 'sungjuk.db'
insert_sungjuk_sql = '''insert into sungjuk(name, kor, eng, mat, tot, avg, grd) values (?, ?, ?, ?, ?, ?, ?)'''
update_sungjuk_sql = '''update sungjuk set kor=?, eng=?, mat=?, tot=?, avg=?, grd=? where sjno=?'''
delete_sungjuk_sql = "delete from sungjuk where sjno = ?"
select_sungjuk_sql = "select sjno, name, kor, eng, mat from sungjuk"
selectone_sungjuk_sql = "select * from sungjuk where sjno = ?"

# 데이터베이스 연결 함수
def make_conn():
    conn = None
    if os.path.exists(dbfile):
        conn = sqlite3.connect(dbfile)
    else:
        print('DB 연결 실패! - 파일이 존재하지 않아요!')
    return conn

# DML 처리함수 1 - 추가, 수정, 삭제
def manuplate_query(sql, params):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    conn.close()


# DML 처리함수 2 - 조회, 상세조회
def retrieve_query(sql, params, fetch):
    conn = make_conn()
    cursor = conn.cursor()
    cursor.execute(sql, params)

    result = None
    if fetch == 'all':
        result = cursor.fetchall()
    elif fetch == 'one':
        result = cursor.fetchone()

    conn.close()
    return result
