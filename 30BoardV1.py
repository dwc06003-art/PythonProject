from dwc06004.boardv1_lib import board
from dwc06004.boardv1_lib import new_board,newone_board,add_board
from dwc06004.boardv1_lib import list_board
from dwc06004.boardv1_lib import view_contents

boards = []


while True:
    job = input(board)
    match job:
        case '1':
            title, userid, contents = new_board()
            bo = newone_board(title, userid, boards)
            add_board(bo, boards)
        case '2':
            list_board(boards)
        case '3':
            view_contents(boards)
        case '4':
            pass
        case '5':
            pass
        case '0':
            print('프로그램을 종료합니다...')
            break
        case _: print('번호를 잘못입력하셨습니다!')


