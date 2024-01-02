def file_load():
    with open('wordlist.txt', 'r') as file:
        word_list = tuple(set(file.read().lower().split('\n')))
    return word_list


def random_word(wordlist: tuple):
    from random import choice
    select_word = choice(wordlist)
    word_len = len(select_word)
    hidden_word = ['_'] * word_len
    return select_word, word_len, hidden_word


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


def word_find(select_word: str, word_len: int, hidden_word: list, guess: str):
    index = -1
    if guess in select_word:
        for i in range(word_len):
            index = select_word.find(guess, index+1)
            if index == -1:
                break
            hidden_word[index] = guess
    else:
        return -1
    return 0


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
    select_word, word_len, hidden_word = random_word(word_list)
    point = 6
    guess_list = []
    loop_check = True
    print_result(hidden_word, guess_list, point)
    while loop_check:
        guess = word_guess(guess_list)
        point += word_find(select_word, word_len, hidden_word, guess)
        loop_check = print_result(hidden_word, guess_list, point)
    print(f'정답: {select_word}')


if __name__ == "__main__":
    main()
