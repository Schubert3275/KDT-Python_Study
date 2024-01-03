def myFunc(a, b):
    return a+b, a-b, a*b, a/b if not b else -1


result = myFunc(10, 3)
print(f'덧셈 결과: {result[0]}, 뺄셈 결과: {result[1]}, 곱셈 결과: {result[2]}, 나눗셈 결과: {result[3]}')

