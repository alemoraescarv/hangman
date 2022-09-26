import random 

class hangman:
    def __init__(self, word_list: list, num_lives: int):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives 
        self.word_guessed = list(len(self.word) * '_')
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = list()

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print("Congrats, your the letter %s is in the word." %guess)
        else:
            print("Sorry your guess %s was not in the word" %guess)

    def ask_for_input(self):
        repeat=True
        while(repeat):
            guess = input("Please input one letter: ")
            if len(guess)==1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You have already taken that letter")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    self.show_letter_guessed(guess)
            else:
                print("Please input only one alphabetical letter!")
            
    def show_letter_guessed(self, letter: str):
        for i in range(0,len(len(self.word))):
            if self.word[i] == letter:
                self.word_guessed.insert(i, letter)
        print(self.word_guessed)

            

