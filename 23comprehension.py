# 컴프리헨션 : 축약
# 시퀀스 자료형(리스트, 딕셔너리등)을
# 한 줄 코드로 간결하게 생성, 관리하는 문법
# 코드를 직관적으로 작성가능 - 한줄로 표현

person = ['혜교', '123-4567-8901', 'abc@abc.co.kr']
for p in person:
    print(p, end = ' ')
print()

# [표현식 for 변수 in 반복가능객체]
[print(p, end =' ') for p in person]
print()

# numbers의 요소를 제곱해서 출력
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print(i * i, end = ' ')
print()

[print(i * i, end = ' ')for i in numbers]
print()

# 1 ~ 100사이 4배수이지만, 6배수는 아닌 수 출력
for i in range(1, 100+1):
    if i % 4 == 0 and i % 6 !=0:
        print(i, end = ' ')
print()

# [표현식 for 변수 in 반복가능객체 if 조건]
[print(i, end = ' ') for i in range(1, 100+1) if i % 4 == 0 and i % 6 !=0]
print()

# numbers 요소를 제곱해서 결과를 리스트로 출력
numbers = [3, 6, 9, 12, 15]
results = []
for i in numbers:
    results.append(i * i)
print(results)

results2 = [i * i for i in numbers]
print(results2)

# 좌석 초기화
seats = []
for i in range(10):
    seats.append('O')
print(seats)

seats = ['O' for i in range(10)]
print(seats)

# 1 ~ 9까지 정수를 3 * 3 2차원 리스트에 출력

matrix = []
# num = 1

for j in range(3):
    row = []
    for i in range(3):
        row.append(i + j * 3 + 1)
        # row.append(num)
        # num += 1
    matrix.append(row)

print(matrix)

# [표현식 for 변수 in 반복가능객체 표현식 for 변수 in 반복가능객체]
# [[표현식 for 변수 in 반복가능객체] 표현식 for 변수 in 반복가능객체]

matrix2 = [i + j * 3 + 1 for j in range(3) for i in range(3)]
print(matrix2)

matrix3 = [[i + j * 3 + 1 for i in range(3)] for j in range(3)]
print(matrix3)