from typing import Tuple, List


class Color:
    """색상용 상수 선언"""
    Reset = '\033[0m'
    Bold = '\033[1m'
    Italic = '\033[3m'
    Underline = '\033[4m'

    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Purple = '\033[95m'
    White = '\033[97m'


def paint(msg, color=Color.White) -> str:
    """색상 적용 편하게 하기 위한 함수"""
    return color+str(msg)+Color.Reset


def file_load() -> Tuple[tuple, str]:
    """txt 파일에서 단어 목록을 읽어와 중복 제거 후 반환"""
    size = size_check()
    filename = 'wordlist_' + size + '.txt'
    with open(filename, 'r') as file:
        wordList = tuple(set(file.read().lower().split('\n')))
    return wordList, size


def size_check() -> str:
    """단어 풀의 크기를 선택하여 해당하는 문자열을 반환"""
    print("1. small   - 약 200개의 단어가 포함되어 있습니다.")
    print("2. big     - 약 800개의 단어가 포함되어 있습니다.")
    print(paint("3. extreme - (주의!) 5만개 이상의 단어가 포함되어 있습니다.", Color.Red))
    size = ''
    while size == '':
        inputSize = input("단어 풀(pool)의 크기를 선택해 주세요 : ")
        if inputSize == '1':
            size = 'small'
        elif inputSize == '2':
            size = 'big'
        elif inputSize == '3':
            size = 'extreme'
        else:
            print("1, 2, 3 중 하나를 입력하세요.")
    return size


def random_word(word_list: tuple) -> Tuple[str, List[str]]:
    """주어진 단어 목록에서 랜덤하게 하나를 추출하고 그 길이만큼 '_' 생성"""
    from random import choice
    selectWord = choice(word_list)
    hiddenWord = ['_' for _ in selectWord]
    return selectWord, hiddenWord


def word_guess(guess_list: List[str], select_word: str) -> str:
    """알파벳 하나를 입력받고 유효성 검사 후 사용한 알파벳 리스트 업데이트, 알파벳 반환"""
    while True:
        guess = input("알파벳을 하나 입력하세요: ").lower().strip()
        if guess == '^^vv<><>ba':  # 코나미 커맨드
            print(f'정답: {select_word}')
        elif is_only_alpha(guess) and len(guess) == 1 and guess not in guess_list:
            guess_list.append(guess)
            guess_list.sort()
            return guess
        elif not is_only_alpha(guess):
            print(paint("a ~ z 사이의 알파벳을 입력해 주세요.", Color.Red))
        elif len(guess) != 1:
            print(paint("한 글자만 입력해 주세요.", Color.Red))
        else:
            print(paint("이미 사용한 글자입니다.", Color.Red))


def is_only_alpha(letters: str) -> bool:
    """a~z까지만 입력받도록 체크"""
    ret = 1
    for letter in letters:
        if letter.isalpha():
            ret *= 1 if ord('a') <= ord(letter) <= ord('z') else 0
        else:
            ret = 0
    return bool(ret)


def word_find(select_word: str, hidden_word: List[str], guess: str) -> int:
    """입력된 알파벳과 문제 단어를 비교. 남은 기회 감산 처리"""
    index = -1
    if guess in select_word:
        for i in range(select_word.count(guess)):
            index = select_word.find(guess, index+1)
            hidden_word[index] = guess
    else:
        return -1
    return 0


def print_result(hidden_word: List[str], guess_list: List[str], point: int, size: str) -> bool:
    """행맨 그림 및 기타 UI 출력"""
    import os
    os.system('cls')
    print(f'\n사용 중인 단어 풀(Pool) - {paint(size, Color.Italic)}', end='')
    print(hangman_aa()[6 - point].rsplit('\n', 5)[0], end='  ')
    print(' '.join(hidden_word))
    print(hangman_aa()[6 - point].rsplit('\n', 5)[1], end='  ')
    print(f'사용한 글자: "{paint(", ".join(guess_list), Color.Green)}"')
    print(hangman_aa()[6 - point].rsplit('\n', 5)[2], end='  ')
    print(f'남은 기회: {print_point_color(point)}')
    print(hangman_aa()[6 - point].split('\n', 5)[5])
    if '_' in hidden_word and point != 0:
        return True
    elif point == 0:
        print(paint("You Lose...", Color.Bold + Color.Yellow))
    else:
        print(paint("You Win!", Color.Bold + Color.Yellow))
    return False


def print_point_color(point: int) -> str:
    """남은 기회에 따라 표시되는 색상 변경"""
    if point >= 5:
        pointColor = paint(point, Color.Blue)
    elif point >= 3:
        pointColor = paint(point, Color.Yellow)
    else:
        pointColor = paint(point, Color.Red)
    return pointColor


def hangman_aa() -> List[str]:
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
    print("행맨(Hangman) 게임을 시작합니다.")
    print("플레이할 단어 풀(Pool)의 크기를 고를 수 있습니다.")
    check = ''
    wordList, size = file_load()
    while check not in ('x', 'X'):
        if check == 'reset':
            wordList, size = file_load()
        selectWord, hiddenWord = random_word(wordList)
        point = 6
        guessList = []
        loopCheck = True
        print_result(hiddenWord, guessList, point, size)
        while loopCheck:
            guess = word_guess(guessList, selectWord)
            point += word_find(selectWord, hiddenWord, guess)
            loopCheck = print_result(hiddenWord, guessList, point, size)
        print(f'정답: {paint(selectWord, Color.Purple)}\n')

        check = input(f"계속하려면 {paint('아무 키', Color.Underline)}나, "
                      f"종료하려면 '{paint('x', Color.Underline)}'를 입력하세요.\n"
                      f"단어 풀(Pool)을 변경하려면 '{paint('reset', Color.Underline)}'을 입력합니다.\n")


if __name__ == '__main__':
    main()
