filename = "wordlist_ori.txt"
wordList = []
wordCount = [0 for _ in range(3, 21)]
print(wordCount)
with open(filename, "r", encoding="utf-8") as file:
    while True:
        word = file.readline().replace('\n', '')
        if word == '':
            break
        if 3 <= len(word) <= 20:
            wordList.append((len(word), word))
            wordCount[len(word)-3] += 1

wordList.sort()
print(wordList, len(wordList))
print(wordCount)

