# 성적 처리프로그램 V3b
# 3명의 학생에 대해
# 이름, 국어, 영어 수학, 점수를 키보드로 입력받아
# 총점, 평균, 학점을 처리한 뒤 결과 출력
# 반복문을 사용해서 코드를 깔끔하게 작성함

result = ''
for i in range(1, 3+1):
    # 입력
    name = input(f'{i}번째 학생 정보 입력 \n이름을 입력하세요 : ')
    kor = int(input(f'{i})국어 점수를 입력하세요 : '))
    eng = int(input(f'{i})영어 점수를 입력하세요 : '))
    math = int(input(f'{i})수학 점수를 입력하세요 : '))
    tot = 0
    avg = 0.0
    grd = 'F'

    # 성적처리
    tot = kor + eng + math
    avg = tot/3
    grd = ('A' if (avg >= 90) else
           'B' if (avg >= 80) else
           'C' if (avg >= 70) else
           'D' if (avg >= 60) else 'F')

    # 결과출력
    result += f'{name:5s} {kor:4d} {eng:4d} {math:4d} {tot:4d} {avg:.2f} {grd:3s}\n'


print(f'''
이름      국어  영어  수학  총점  평균 학점
--------------------------------
{result}
''')
