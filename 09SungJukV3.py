# 성적 처리프로그램 V3
# 3명의 학생에 대해
# 이름, 국어, 영어 수학, 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력

# 입력
name = input('1번째 학생 정보 입력 \n이름을 입력하세요 : ')
kor = int(input('국어 점수를 입력하세요 : '))
eng = int(input('영어 점수를 입력하세요 : '))
math = int(input('수학 점수를 입력하세요 : '))

name2 = input('2번째 학생 정보 입력 \n이름을 입력하세요 : ')
kor2 = int(input('국어 점수를 입력하세요 : '))
eng2 = int(input('영어 점수를 입력하세요 : '))
math2 = int(input('수학 점수를 입력하세요 : '))

name3 = input('3번째 학생 정보 입력 \n이름을 입력하세요 : ')
kor3 = int(input('국어 점수를 입력하세요 : '))
eng3 = int(input('영어 점수를 입력하세요 : '))
math3 = int(input('수학 점수를 입력하세요 : '))

# 처리
tot = kor + eng + math
avg = tot/3
grd = ('A' if (avg >= 90) else
       'B' if (avg >= 80) else
       'C' if (avg >= 70) else
       'D' if (avg >= 60) else 'F')

tot2 = kor2 + eng2 + math2
avg2 = tot2 / 3
grd2 = ('A' if (avg2 >= 90) else
       'B' if (avg2 >= 80) else
       'C' if (avg2 >= 70) else
       'D' if (avg2 >= 60) else 'F')

tot3 = kor3 + eng3 + math3
avg3 = tot3/3
grd3 = ('A' if (avg3 >= 90) else
       'B' if (avg3 >= 80) else
       'C' if (avg3 >= 70) else
       'D' if (avg3 >= 60) else 'F')

# 출력
pfmt = f'''
이름   국어 영어 수학  총점   평균  학점
--------------------------------
{name}  {kor}  {eng}  {math}  {tot}  {avg:.2f}  {grd}
{name2}  {kor2}  {eng2}  {math2}  {tot2}  {avg2:.2f}  {grd2}
{name3}  {kor3}  {eng3}  {math3}  {tot3}  {avg3:.2f}  {grd3} 
'''
print(pfmt)