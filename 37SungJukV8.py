# 성적 처리프로그램 V8
# 이름, 국어, 영어 수학, 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력 - 학생번호도 추가
# 성적처리의 CRUD를 메뉴식으로 구현
# 성적 데이터를 csv파일에 저장
#     1,'혜교',99,98,99,297,99.99,'A'
#     2,'지연',33,44,55,197,77.82,'C'
#     3,'수지',77,88,99,235,85.99,'B'
# 성적처리 CRUD 기능 함수로 구조화 : 모듈명 sungjukv7_lib
# 예외처리 코드 추가 - input_sungjuks, modify_sungjuk, remove_sungju, load_sungjuk
# 예외 발생시 로깅메세지도 추가 - sungjuk_logging, sungjukv8.log

from dwc06004.sungjukv8_lib import menus
from dwc06004.sungjukv8_lib import header1, header2
from dwc06004.sungjukv8_lib import input_sungjuk, compute_sungjuk, add_sungjuk
from dwc06004.sungjukv8_lib import readall_sungjuk
from dwc06004.sungjukv8_lib import readone_sungjuk
from dwc06004.sungjukv8_lib import modify_sungjuk
from dwc06004.sungjukv8_lib import remove_sungjuk
from dwc06004.sungjukv8_lib import load_sungjuk
from dwc06004.sungjukv8_lib import write_sungjuk
from dwc06004.sungjukv8_lib import sungjuk_logging


# sungjuk.csv로 부터 저장된 성적데이터를 모두 읽어
# sungjuks 변수에 저장
sungjuk_logging()
sungjuks = load_sungjuk()

while True:
    job = input(menus)
    match job:
        case '1':
            name, kor, eng, math = input_sungjuk()
            if name != '0':
                sj = compute_sungjuk(name, kor, eng, math)
                add_sungjuk(sj, sungjuks)
                write_sungjuk(sungjuks)

        case '2':
            readall_sungjuk(sungjuks)

        case '3':
            readone_sungjuk(sungjuks)
        case '4':
            modify_sungjuk(sungjuks)
            write_sungjuk(sungjuks)
        case '5':
            remove_sungjuk(sungjuks)
            write_sungjuk(sungjuks)
        case '0':
            print('성적프로그램을 종료합니다...')
            break
        case _: print('번호를 잘못입력하셨습니다!')