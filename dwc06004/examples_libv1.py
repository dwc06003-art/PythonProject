def compute_tax(isMarried, salary):
    """
    결혼여부와 연봉을 입력하면 세율과 세금을 계산해 줍니다

    Parameters:
        isMarried : 결혼여부
        salary : 연봉

    Returns:
        list: (rate, tax)
            - int : 세율
            - float : 세금
    """
    tax, rate = 0, 0

    match isMarried:
        case 'n':
            rate = 25
            if salary < 3000: rate = 10
        case 'y':
            rate = 25
            if salary < 3000: rate = 10
        case _:
            print('결혼여부 오류!!')

    tax = salary * (rate / 100)

    return rate, tax


def count_mathes(mykey, lotto):
    """
    로또 일치여부를 확인하는 함수

    :param mykey:
    :param lotto:
    :return:

    """
    match = 0
    for i in range(3):
        for j in range(3):
            if lotto[i] == mykey[j]: match += 1
    return match


def get_prize(match):
    """
    로또 일치여부에 따라 상금 조회하는 함수

    :param match:
    :return:
    """
    prize = 0
    if match == 3: prize = 1000000
    elif match == 2: prize = 10000
    elif match == 1: prize = 1000
    return prize


def generate_gugudan(dan):
    """
    단을 입력받아 구구단 출력하는 함수

    :param dan:
    :return:
    """
    if 1 <= dan <= 9:
        result = f'==={dan}단===\n'
        for i in range(1, 10):
            result += f'{dan} * {i} = {dan * i}\n'
    else:
        result = '잘못입력하셨습니다!'

    return result


def check_Jumin(jumin):
    """
    입력한 주민번호가 올바른 것인지 확인하는 함수

    :param jumin:
    :return:
    """
    sum = 0
    code = [int(j) for j in jumin if j.isdigit()]

    wght = [i % 8 + 2 for i in range(12)]

    for i in range(12):
        sum += code[i] * wght[i]

    checker = 11 - (sum % 11)
    isvalid = str(checker)[-1] == jumin[13]

    return code, wght, sum, isvalid
