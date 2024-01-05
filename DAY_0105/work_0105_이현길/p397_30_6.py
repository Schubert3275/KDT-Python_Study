"""
30.6 연습문제: 가장 높은 점수를 구하는 함수 만들기
"""
korean, english, mathematics, science = 100, 86, 81, 91


def get_max_score(*args):
    return max(args)


max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)
