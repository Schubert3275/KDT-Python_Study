class Color:
    Reset = '\033[0m'
    Bold = '\033[1m'
    Italic = '\033[3m'
    Underline = '\033[4m'

    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Purple = '\033[95m'
    Cyan = '\033[96m'


def file_load() -> tuple:
    """txt 파일에서 단어 목록 중복 제거하여 튜플 형태로 반환"""
    with open('wordlist.txt', 'r') as file:
        word_list = tuple(set(file.read().lower().split('\n')))
    return word_list


def random_word(wordlist: tuple):
    """주어진 단어 목록에서 랜덤하게 하나를 추출하고 그 길이만큼 '_' 생성"""
    from random import choice
    select_word = choice(wordlist)
    # select_word = 'testwordsample'
    hidden_word = ['_'] * len(select_word)
    return select_word, hidden_word


def word_guess(guess_list: list, select_word: str) -> str:
    """알파벳 하나를 입력받고 유효성 검사 후 사용한 알파벳 리스트 업데이트 및 유효 알파벳 반환"""
    while True:
        guess = input("알파벳을 하나 입력하세요: ").lower().strip()
        if guess == 'cheatcode':
            print(f'정답: {select_word}')
        elif is_only_alpha(guess) and len(guess) == 1 and guess not in guess_list:
            guess_list.append(guess)
            guess_list.sort()
            return guess
        elif not is_only_alpha(guess):
            print(Color.Red + "a ~ z 사이의 알파벳을 입력해 주세요." + Color.Reset)
        elif len(guess) != 1:
            print(Color.Red + "한 글자만 입력해 주세요." + Color.Reset)
        else:
            print(Color.Red + "이미 사용한 글자입니다." + Color.Reset)


def is_only_alpha(letters: str) -> bool:
    ret = 1
    for letter in letters:
        if letter.isalpha():
            ret *= 1 if ord('a') <= ord(letter) <= ord('z') else 0
    return bool(ret)


def word_find(select_word: str, hidden_word: list, guess: str) -> int:
    """입력된 알파벳과 문제 단어를 비교하여 정답 가부 처리"""
    index = -1
    if guess in select_word:
        for i in range(select_word.count(guess)):
            index = select_word.find(guess, index+1)
            hidden_word[index] = guess
    else:
        return -1
    return 0


def print_result(hidden_word: list, guess_list: list, point: int) -> bool:
    """행맨 그림 및 기타 UI 출력"""
    print(hangman_aa()[6 - point].rsplit('\n', 5)[0], end='  ')
    print(' '.join(hidden_word))
    print(hangman_aa()[6 - point].rsplit('\n', 5)[1], end='  ')
    print(f'사용한 글자: "{Color.Green}{", ".join(guess_list)}{Color.Reset}"')
    print(hangman_aa()[6 - point].rsplit('\n', 5)[2], end='  ')
    print(f'남은 기회: {print_point_color(point)}')
    print(hangman_aa()[6 - point].split('\n', 5)[5])
    if '_' in hidden_word and point != 0:
        return True
    elif point == 0:
        print(Color.Bold + Color.Yellow + "You Lose!" + Color.Reset)
    else:
        print(Color.Bold + Color.Yellow + "You Win!" + Color.Reset)
    return False


def print_point_color(point: int):
    if point >= 5:
        point_color = Color.Blue + str(point) + Color.Reset
    elif point >= 3:
        point_color = Color.Yellow + str(point) + Color.Reset
    else:
        point_color = Color.Red + str(point) + Color.Reset
    return point_color


def hangman_aa() -> list:
    """행맨 아스키 아트"""
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
    check = ''
    print("행맨(Hangman) 게임을 시작합니다.")
    while check not in ('x', 'X'):
        word_list = file_load()
        select_word, hidden_word = random_word(word_list)
        point = 6
        guess_list = []
        loop_check = True
        print_result(hidden_word, guess_list, point)
        while loop_check:
            guess = word_guess(guess_list, select_word)
            point += word_find(select_word, hidden_word, guess)
            loop_check = print_result(hidden_word, guess_list, point)
        print(f'정답: {Color.Bold}{select_word}{Color.Reset}\n')

        check = input("계속하려면 아무 키나, 종료하려면 'X'를 입력하세요.\n")


if __name__ == '__main__':
    main()
