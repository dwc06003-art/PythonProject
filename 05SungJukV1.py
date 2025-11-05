# 성적 처리프로그램 V1
# 이름, 국어, 영어, 수학 점수를 변수로 설정하고
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 단, 학점은 삼항연산자를 이용해서 계산한다
# 변수 = 참일때 값 if 조건식 else 거짓일때 값
from sys import api_version

# 입력
# 이름, 국어, 영어, 수학 점수를 변수로 설정
name = '김민수'
language = 99
english = 99
math = 98

# 성적처리
# 총점, 평균, 학점을 처리
total =(language + english + math)
average = (total / 3)
score = average
# grd = 'A' if(score >= 90) else 'B'
grd = ('A' if (score >= 90) else
       'B' if (score >= 80) else
       'C' if (score >= 70) else
       'D' if (score >= 60) else 'F')

# 결과 출력
# 이름, 국어, 영어, 수학, 총점, 평균, 학점 출력
print('=====성적결과=====')
print('이름 :', name)
print('국어 :', language)
print('영어 :', english)
print('수학 :', math)
print('총점 :', total)
print(f'평균 : {average:.2f}')
print('학점 :', grd)