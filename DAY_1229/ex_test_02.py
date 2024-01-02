# -------------------------------------------------------------------
# [실습1] 임의의 숫자 데이터 7개를 저장한 리스트를 생성
#         리스트에 원소를 화면에 한 줄에 한 개씩 출력하세요.
# -------------------------------------------------------------------
list1 = [1, 2, 3, 4, 5, 6, 7]
print(list1[0], list1[1], list1[2], list1[3], list1[4], list1[5], list1[6], sep='\n')
print('-' * 50)

# -------------------------------------------------------------------
# [실습2] 아래 리스트에서 원소를 화면에 한 줄에 한 개씩 출력하세요.
# -------------------------------------------------------------------
datas = [[10, 20], [40, 50], [70, 80, 90]]
#         0         1         2
#         0   1     0   1     0   1   2
print(datas[0][0], datas[0][1],
      datas[1][0], datas[1][1],
      datas[2][0], datas[2][1], datas[2][2], sep='\n')
print('-' * 50)

# -------------------------------------------------------------------
# [실습3] 좋아하는 계절과 월(month)을 입력 받은 후 각각 변수에
#         저장하세요.
#         변수명은 season, month 입니다.
#         input()함수는 1개만 사용하세요.
# -------------------------------------------------------------------
season, month = input("좋아하는 계절과 월 입력 (예:겨울,12): ").split(',')
print(f'좋아하는 계절은 {season}, 좋아하는 월은 {month}월입니다.')
print('-' * 50)

# -------------------------------------------------------------------
# [실습4] 1~20으로 구성된 정수 리스트를 생성하세요.
#         * 3의 배수 인덱스에 해당하는 정수만 출력하세요.
#         * 3의 배수 인덱스에 해당하는 정수의 합계를 출력하세요.
# -------------------------------------------------------------------
# numList = [i for i in range(1, 21)]
# numList = list(range(1, 21))
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# print('3의 배수 인덱스 정수:', ' '.join(map(str, numList[3::3])))
print('3의 배수 인덱스 정수:', numList[3], numList[6], numList[9], numList[12], numList[15], numList[18])
# print(3의 배수 인덱스 정수의 합:', sum(numList[3::3]))
print('3의 배수 인덱스 정수의 합:', numList[3] + numList[6] + numList[9] + numList[12] + numList[15] + numList[18])