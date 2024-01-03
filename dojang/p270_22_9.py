"""
22.9 연습문제: 리스트에서 특정 요소만 뽑아내기
"""
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]

print(b)
