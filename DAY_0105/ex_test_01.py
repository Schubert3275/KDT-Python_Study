from typing import Union
# -----------------------------------------------------------------------------
# [실습1]  2개의 정수를 입력 받은 후 사칙연산 수행 결과를 반환하는 기능의
#          함수를 정의해 주세요.
#          함수이름 : fourCalc
#          매개변수 : n1, n2
#          반환결과 : 사칙연산 결과
# -----------------------------------------------------------------------------


def fourCalc(n1: Union[int, float], n2: Union[int, float]) -> tuple:
    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else '0으로 나눌 수 없음'


# -----------------------------------------------------------------------------
# [실습2]  문자열을 16진수 코드값으로 변환 후 반환하는 함수를 정의해 주세요.
#          함수이름 : getCode
#          매개변수 : message
#          반환결과 : str
# -----------------------------------------------------------------------------
def getCode(message: str) -> str:
    wordStr = ''
    for idx, word in enumerate(message):
        wordStr += f'{hex(ord(word))}' + (' ' if idx != len(message)-1 else '')
    return wordStr


print(fourCalc(10, 5))
print(fourCalc(10, 0))

print(getCode('Good Luck'))
