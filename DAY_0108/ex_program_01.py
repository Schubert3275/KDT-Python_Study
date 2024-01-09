# -------------------------------------------------------------------------------------------------
# 나의 프로그램 : 계산기
# [계산기]
# 1. 입력
# 2. 덧셈
# 3. 뺄셈
# 4. 곱셈
# 5. 나눗셈
# 6. 종료
# -------------------------------------------------------------------------------------------------
# 사용자 정의 함수  -------------------------------------------------------------------------------
# 함수 기능 : 연산결과 리스트에서 검색어에 해당하는 데이터만 출력
# 함수 이름 : searchResult
# 매개 변수 : search
# 함수 결과 : none
# -------------------------------------------------------------------------------------------------
def searchResult(search):
    cnt = 0
    for calc in calcList:
        if search in calc:
            print(calc)
            cnt += 1
    print(f'{cnt}개 검색 결과가 있습니다' if cnt else '검색 결과가 없습니다.')


# 계산기록 저장할 전역변수 선언 -------------------------------------------------------------------
calcList = []
while True:
    print("[나의 계산기]")
    print(" 1. 입  력")
    print(" 2. 덧  셈")
    print(" 3. 뺄  셈")
    print(" 4. 곱  셈")
    print(" 5. 나눗셈")
    print(" 6. 기록보기")
    print(" 7. 검  색")
    print(" 8. 기록삭제")
    print(" 9. 종  료")
    choice = input("메뉴 선택 : ")
    if choice.isdecimal():
        if choice == '1':
            data = input("2개 정수(예: 10 20) : ")
            n1, n2 = list(map(int, data.split()))
        elif choice == '2':
            calcList.append(f'덧셈 결과 : {n1} + {n2} = {n1 + n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '3':
            calcList.append(f'뺄셈 결과 : {n1} - {n2} = {n1 - n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '4':
            calcList.append(f'곱셈 결과 : {n1} * {n2} = {n1 * n2}')
            print(f'{calcList[-1]}\n')
        elif choice == '5':
            calcList.append(f'나눗셈 결과 : {n1} / {n2} = {n1 / n2 if n2 else "0으로 나눌 수 없음"}')
            print(f'{calcList[-1]}\n')
        elif choice == '6':
            print("==> 계산 기록")
            print('\n'.join(calcList))
        elif choice == '7':
            search = input("검  색 : ")
            searchResult(search)
        elif choice == '8':
            calcList.clear()
            print("모든 계산 기록이 삭제되었습니다.")
        elif choice == '9':
            print("프로그램 종료합니다.")
            break
        else:
            print("메뉴는 1 ~ 9까지 선택 가능합니다.")
    else:
        print("없는 메뉴입니다.")
