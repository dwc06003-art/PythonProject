board = f'''
===== 게시판 프로그램 =====
1. 새 글쓰기
2. 글 목록
3. 본문 보기
4. 글 수정
5. 글 삭제
0. 종료
메뉴를 선택하세요 : '''

header1 = '''
=====게시글 목록=====
번호 | 제목 | 작성자 | 조회수 | 작성일
-------------------------------
'''

header2 = '''
===== 본문 내용 =====
'''

def new_board():
    title = input(f'글제목 : ')
    userid = input(f'작성자 : ')
    contents = input(f'본문 : ')

    return title, userid, contents

def newone_board(title, userid, boards, contents):
    bno = len(boards) + 1
    views = 0

    return [bno, title, userid, contents, views]

def add_board(bo, boards):

    boards.append(bo)

def list_board(boards):
    result = ''
    for bno, title, userid, contents, views in boards:
        result += f'{bno} | {title:3s} | {userid:3s} | {views:3d}\n'

    print(f'{header1}{result}')

def view_contents(boards):
    result = ''
    for bno, title, userid, contents, views in boards:
        result = f'''
                글번호 : {bno}
                제목 : {title}
                작성자 : {userid}
                본문 : {contents}
                조회수 : {views}
                작성일 : 
                '''

    print(f'{header1}{result}')