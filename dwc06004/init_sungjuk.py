import os
import sqlite3

dbfile = '../sungjuk.db'

# 멱등성 :
# create table if not exists
# 한 작업을 여러번 실행해도 결과가 처음 실행하 것과 동일하게 유지되는 성질
sql = ''' create table if not exists sungjuk(
sjno integer primary key autoincrement,
name varchar(10) not null,
kor int, eng int, mat int,
tot int, avg float, grd char(1),
regdate datetime default current_timestamp
)'''

# sqlite3 디비 파일 생성용 코드 - 한번만 실행
# conn = sqlite3.connect(dbfile)
# conn.close()

# 디비 파일 존재 여부 확인
if os.path.exists(dbfile):
    conn = sqlite3.connect(dbfile)
    print('DB 연결 성공!!')

    cursor = conn.cursor()

    # 쿼리 작성후 실행
    cursor.execute(sql)
    print('성적테이블생성완료!')

    conn.close()

else:
    print('DB 연결 실패! - 파일이 존재하지 않아요!')