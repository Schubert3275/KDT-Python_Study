"""
22.10 심사문제: 2의 거듭제곱 리스트 생성하기
"""
num1, num2 = map(int, input().split())

nums = [2**n for n in range(num1, num2+1) if n != num1+1 and n != num2-1]
print(nums)
