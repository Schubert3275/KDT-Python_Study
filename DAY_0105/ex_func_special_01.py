# -----------------------------------------------------------------------------
# 다양한 함수의 형태 - 특별한 함수 (1)
# - 매개변수의 갯수를 유동적으로 가변으로 하는 함수
# - 형태 : def 함수명( *data ):
# - 가변인자 함수
# - 매개변수 갯수 : 0개 ~ N개
# -----------------------------------------------------------------------------
# 2개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------------------------
def addTwo(num1, num2):
    return num1 + num2


# 5개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------------------------
def addFive(num1, num2, num3, num4, num5):
    return num1 + num2 + num3 + num4 + num5


# 3개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------------------------
def addThree(num1, num2, num3):
    return num1 + num2 + num3


# 7개 정수를 덧셈 후 결과를 반환하는 함수 생성 --------------------------------
def addSeven(num1, num2, num3, num4, num5, num6, num7):
    return num1 + num2 + num3 + num4 + num5 + num6 + num7


# -----------------------------------------------------------------------------
# 함수 기능 : 전달받은 숫자를 모두 덧셈한 결과 반환 기능
# 함수 이름 : addNumber
# 매개 변수 : *nums
# 반환값    : 계산 결과
# -----------------------------------------------------------------------------
def addNumber(*nums: int):
    print(type(nums))
    ret = 0
    for d in nums:
        ret += d
    return ret


# 함수 사용 즉 함수 호출 ------------------------------------------------------
print(addNumber(1, 2, 3))
print(addNumber(10))
print(addNumber())
print(addNumber(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# *시퀀스/반복이 가능한 객체 => 내부의 모든 원소를 하나씩 풀어서 전달 : 언패킹
print(addNumber(*range(1, 11)))

a = [11, 22, 33, 44]
aTuple = 'a', 'b', 'c'
aDict = {'jj': 'Hong', 'age': 100}

print(a, aTuple, aDict)
print(*a, *aTuple, sep='-')
print(*aDict, sep='-')