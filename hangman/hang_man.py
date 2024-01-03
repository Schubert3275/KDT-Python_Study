# txt 파일에서 단어 목록 중복 제거하여 튜플 형태로 반환
def file_load():
    with open('wordlist.txt', 'r') as file:
        word_list = tuple(set(file.read().lower().split('\n')))
    return word_list


# 주어진 단어 목록에서 랜덤하게 하나를 추출하고 그 길이만큼 '_' 생성
def random_word(wordlist: tuple):
    from random import choice
    select_word = choice(wordlist)
    # select_word = 'testwordsample'
    hidden_word = ['_'] * len(select_word)
    return select_word, hidden_word


# 알파벳 하나를 입력받고 유효성 검사 후 사용한 알파벳 리스트 업데이트 및 유효 알파벳 반환
def word_guess(guess_list: list):
    while True:
        guess = input("알파벳을 하나 입력하세요: ").lower().strip()
        if guess.isalpha() and len(guess) == 1 and guess not in guess_list:
            guess_list.append(guess)
            guess_list.sort()
            return guess
        elif not guess.isalpha():
            print("알파벳을 입력해 주세요.")
        elif len(guess) != 1:
            print("한 글자만 입력해 주세요.")
        else:
            print("이미 사용한 글자입니다.")


# 입력된 알파벳과 문제 단어를 비교하여 정답 가부 처리
def word_find(select_word: str, hidden_word: list, guess: str):
    index = -1
    if guess in select_word:
        for i in range(select_word.count(guess)):
            index = select_word.find(guess, index+1)
            hidden_word[index] = guess
    else:
        return -1
    return 0


# 행맨 그림 및 기타 UI 출력
def print_result(hidden_word: list, guess_list: list, point: int):
    print(hangman_aa()[6 - point].rsplit('\n', 5)[0], end='  ')
    print(' '.join(hidden_word))
    print(hangman_aa()[6 - point].rsplit('\n', 5)[1], end='  ')
    print(f'사용한 글자: "{", ".join(guess_list)}"')
    print(hangman_aa()[6 - point].rsplit('\n', 5)[2], end='  ')
    print(f'남은 기회: {point}')
    print('\n'.join(hangman_aa()[6 - point].rsplit('\n', 5)[3:]))
    if '_' in hidden_word and point != 0:
        return True
    elif point == 0:
        print("You Lose!")
    else:
        print("You Win!")
    return False


# 행맨 아스키 아트
def hangman_aa():
    asciiart = [r'''
 +───+
 │   │   
 │       
 │       
 │       
 │       
=========''', r'''
 +───+
 │   │   
 │   O   
 │       
 │       
 │       
=========''', r'''
 +───+
 │   │   
 │   O   
 │   │   
 │       
 │       
=========''', r'''
 +───+
 │   │   
 │   O   
 │  /│   
 │       
 │       
=========''', r'''
 +───+
 │   │   
 │   O   
 │  /│\  
 │       
 │       
=========''', r'''
 +───+
 │   │   
 │   O   
 │  /│\  
 │  /    
 │       
=========''', r'''
 +───+   
 │   │   
 │   O   
 │  /│\  
 │  / \  
 │       
=========''']
    return asciiart


def main():
    word_list = file_load()
    select_word, hidden_word = random_word(word_list)
    point = 6
    guess_list = []
    loop_check = True
    print_result(hidden_word, guess_list, point)
    while loop_check:
        guess = word_guess(guess_list)
        point += word_find(select_word, hidden_word, guess)
        loop_check = print_result(hidden_word, guess_list, point)
    print(f'정답: {select_word}')


if __name__ == "__main__":
    main()
