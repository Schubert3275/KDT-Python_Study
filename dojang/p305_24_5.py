"""
24.5 심사문제: 특정 단어 개수 세기
"""
msg = """the grown-ups' response, this time, was to advise me to lay aside my drawing of boa constrictors,
whether from the inside or the outside, and devote myself instead to geography, history, arithmetic,
and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as
a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two.
Grown-ups never understand anything by themselves, and it is tiresome for children to be always and
forever explaining things to the."""

# msg = input()

msg = msg.replace('.', '')
msg = msg.replace(',', '')
msg_find = msg.split()
count = msg_find.count('the')
print(count)
