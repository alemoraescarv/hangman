import random
import string


       

def ask_for_input(word: string):
    """ Function to ask for intput
    :input: word: string
    :return: None"""
    repeat=True
    while(repeat):
        guess = input("Please input one letter: ")
        if len(guess)==1:
            repeat=False
        else:
            print("Please input only one letter!")
    check_guess(guess,word)

def check_guess(guess: string, word: string):
    """Function to check if the guess is in the word
    :input: guess: string
    :input: word: string
    :return: None"""
    guess = guess.lower()
    if guess in word:
        print("Congrats, your the letter %s is in the word." %guess)
    else:
        print("Sorry your guess %s was not in the word" %guess)   
    

if __name__=="__main__":
    ask_for_input("apple")