# 게시판 앱 V1
# "글번호, 글제목, 작성자, 본문, 조회수, 작성일" 형식의
# 게시판 데이터를 생성, 조회, 수정, 삭제 하는 프로그램
# 새글쓰기 : 글제목, 작성자, 본문
# 게시판 목록 : 글번호, 글제목, 작성자, 조회수, 작성일(년월일)
# 본문보기 : 글번호, 글제목, 작성자, 본문, 조회수, 작성일

from dwc06004.boardv1_lib_a import menus
from dwc06004.boardv1_lib_a import write_board
from dwc06004.boardv1_lib_a import list_board
from dwc06004.boardv1_lib_a import view_board
from dwc06004.boardv1_lib_a import modify_board
from dwc06004.boardv1_lib_a import remove_board

boards = []


while True:
    job = input(menus)

    match job:
        case '1':
            write_board(boards)
        case '2':
            list_board(boards)

        case '3':
            view_board(boards)

        case '4':
            modify_board(boards)

        case '5':
            remove_board(boards)

        case '0': break
        case _: print('번호를 잘못 입력하셨습니다!')