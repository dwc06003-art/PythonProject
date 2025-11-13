# 32 주민번호 검사 - 리스트, 컴프리헨션으로 재작성
# 문자가 숫자인지 확인 : isdigit()
jumin = '581131-1974523'
sum = 0

# a, b
# code = []
# for j in jumin:
#     if j.isdigit():
#         code.append(int(j))
# print(f'추출된 주민번호 : {code}')

code = [int(j) for j in jumin if j.isdigit()]
print(f'추출된 주민번호 : {code}')

# wght = [2,3,4,5,6,7,8,9,2,3,4,5]
# wght = []
# for i in range(12):
#     wght.append(i % 8 + 2)

wght = [i % 8 + 2 for i in range(12)]

print(f'자동생성된 가중치 : {wght}')

for i in range(12):
    sum += code[i] * wght[i]
print(sum)

# c,d
checker = 11 - (sum % 11)
print(checker, str(checker)[-1] == jumin[13])
