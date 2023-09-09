import random
import os
import time

list_of_words = []

def drow_hangman(line, count_of_errors, word):
    if line == word:
        if count_of_errors == 1:
            print('   _____ \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '  |      \n'
                '__|__\n')
        elif count_of_errors == 2:
            print('   _____ \n'
                  '  |     | \n'
                  '  |     | \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '__|__\n')
        elif count_of_errors == 3:
            print('   _____ \n'
                  '  |     | \n'
                  '  |     | \n'
                  '  |     o \n'
                  '  |      \n'
                  '  |      \n'
                  '  |      \n'
                  '__|__\n')
        elif count_of_errors == 4:
            print('   _____ \n'
                  '  |     | \n'
                  '  |     | \n'
                  '  |     o \n'
                  '  |    /|\ \n'
                  '  |      \n'
                  '  |      \n'
                  '__|__\n')
        elif count_of_errors == 5:
            print('   _____ \n'
                  '  |     | \n'
                  '  |     | \n'
                  '  |     o \n'
                  '  |    /|\ \n'
                  '  |     | \n'
                  '  |      \n'
                  '__|__\n')
        print("you win!\n")
        restart()
    elif count_of_errors == 0:
        main_game(line, count_of_errors, word)
    elif count_of_errors == 1:
        print('   _____ \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '__|__\n')
        main_game(line, count_of_errors, word)
    elif count_of_errors == 2:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '__|__\n')
        main_game(line, count_of_errors, word)
    elif count_of_errors == 3:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |     o \n'
              '  |      \n'
              '  |      \n'
              '  |      \n'
              '__|__\n')
        main_game(line, count_of_errors, word)
    elif count_of_errors == 4:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |     o \n'
              '  |    /|\ \n'
              '  |      \n'
              '  |      \n'
              '__|__\n')
        main_game(line, count_of_errors, word)
    elif count_of_errors == 5:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |     o \n'
              '  |    /|\ \n'
              '  |     | \n'
              '  |      \n'
              '__|__\n')
        main_game(line, count_of_errors, word)
    elif count_of_errors == 6:
        print('   _____ \n'
              '  |     | \n'
              '  |     | \n'
              '  |     o \n'
              '  |    /|\ \n'
              '  |     | \n'
              '  |    / \ \n'
              '__|__      \n')
        print("you lose(\n")

        restart()


def restart():
    done = False
    while not done:
        command = str(input("[R]estart [E]xit\n"))
        if command == "R":
            word = random.choice(list_of_words)
            len_of_word = len(word)
            count_of_errors = 0
            line = '*'*len_of_word
            os.system("clear")
            main_game(line, count_of_errors, word)

        elif command == "E":
            os.system("clear")
            exit()

        else:
            os.system("clear")
            print("Введите правильную команду!")
            

def main_game(line, count_of_errors, word):

    letter = str(input(f"The word is:\n{line}\n\nenter the letter:\n"))
    os.system("clear")

    if len(letter) != 1:
        print("Enter only one letter")

    elif letter in word:
        list_of_indexex = []

        for index, char in enumerate(word):
            if char == letter:
                list_of_indexex.append(index)

        l_line = list(line)

        for i in range(len(list_of_indexex)):
            l_line[list_of_indexex[i]] = letter
        line = "".join(l_line)

    elif letter not in word:
        print('not correct')
        count_of_errors += 1

    
    drow_hangman(line, count_of_errors, word)
    

if __name__ == "__main__":
    ready = False
    os.system("clear")
    while not ready:
        command_for_words = str(input("Do you have your own list of words?\n[Y]es [N]o\n"))
        if command_for_words == "Y":
            f = open('/Users/p4sh4bsc/python_projects/hangman/words.txt')
            for line in f:
                list_of_words.append(line.strip())
            ready = True
        elif command_for_words == "N":
            list_of_words = ["car", "home", "headphones", "nature", "phone", "oil", "book", "aple", "index", "future"]
            ready = True
        else:
            os.system("clear")
            print("Your input is not correct\n Y or N")  

    os.system("clear")

    word = random.choice(list_of_words)
    len_of_word = len(word)
    count_of_errors = 0
    line = '*'*len_of_word

    main_game(line, count_of_errors, word)