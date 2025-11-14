# 성적 처리프로그램 V6
# 이름, 국어, 영어 수학, 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 성적처리의 CRUD를 메뉴식으로 구현
# 성적 데이터를 시퀀스 자료형에 저장
# 성적처리 CRUD 기능 함수로 구조화 : 모듈명 sungjukv6_lib

from dwc06004.sungjukv6_lib import menus
from dwc06004.sungjukv6_lib import header1, header2
from dwc06004.sungjukv6_lib import input_sungjuk, compute_sungjuk, add_sungjuk
from dwc06004.sungjukv6_lib import readall_sungjuk
from dwc06004.sungjukv6_lib import readone_sungjuk
from dwc06004.sungjukv6_lib import modify_sungjuk
from dwc06004.sungjukv6_lib import remove_sungjuk

sungjuks = []   #성적데이터 저장용 변수

while True:
    job = input(menus)
    match job:
        case '1':
            name, kor, eng, math = input_sungjuk()
            sj = compute_sungjuk(name, kor, eng, math)
            add_sungjuk(sj, sungjuks)

        case '2':
            readall_sungjuk(sungjuks)

        case '3':
            readone_sungjuk(sungjuks)
        case '4':
            modify_sungjuk(sungjuks)
        case '5':
            remove_sungjuk(sungjuks)
        case '0':
            print('성적프로그램을 종료합니다...')
            break
        case _: print('번호를 잘못입력하셨습니다!')
