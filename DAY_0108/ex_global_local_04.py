# -------------------------------------------------------------------------------------------------
#
# -------------------------------------------------------------------------------------------------
def one(number):
    print(number)


def datas(nums, value):
    # nums : 리스트
    # value : 정수
    nums[-1] = 1004
    value = 'HAPPY'
    print(nums, value, sep=' - ')


# 전역 변수 선언 ----------------------------------------------------------------------------------
value = 'Good'
dataList = [11, 22, 33]
num = 7

# 함수 호출 ---------------------------------------------------------------------------------------
print(f'전역변수값 => value : {value}, dataList : {dataList}, num : {num}')

one(num)
datas(dataList, value)

print(f'전역변수값 => value : {value}, dataList : {dataList}, num : {num}')


