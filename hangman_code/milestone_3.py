import random 

class Hangman:
    def __init__(self, word_list: list, num_lives: int):
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.num_lives = num_lives 
        self.word_guessed = list(len(self.word) * '_')
        self.num_letters = len(set(self.word)) 
        self.list_of_guesses = list()

    def check_guess(self, guess):
        """Check if guess is in word, reduce lives and number of chars in a word"""
        guess = guess.lower()
        if guess in self.word:
            print("Congrats, your the letter %s is in the word." %guess)
            #self.show_letter_guessed(guess)
        else:
            print("Sorry your guess %s was not in the word" %guess)
            self.num_lives-=1
            print("You have {} lives".format(self.num_lives))

    def ask_for_input(self):
        """Function to ask for input , guess to lower letter"""
        repeat=True
        while(repeat):
            guess = input("Please input one letter: ")
            if len(guess)==1 and guess.isalpha():
                if guess in self.list_of_guesses:
                    print("You have already chosen that letter")
                else:
                    self.check_guess(guess)
                    self.list_of_guesses.append(guess)
                    self.show_letter_guessed(guess)
            else:
                print("Please input only one alphabetical letter!")
            if self.num_letters < 0:
                break
            if self.num_lives < 0:
                break
            
    def show_letter_guessed(self, letter: str):
        """Function to print the letter guesses and the word with _ for the non guessed ones
        :input: letter: Char : guesses letter"""
        for i in range(0,len(self.word)):
            if self.word[i] == letter:
                self.num_letters-=1
                self.word_guessed[i] = letter
        print(self.word_guessed)

class Game(Hangman):
    def __init__(self):
        super().__init__(["apple"],5)

    def play_game(self):
        """Function to run the game, loop through the ask input and check won or lost
        """
        #word_list = ["strawberry","apple","kiwi","banana","mango"]
        game = Hangman(self.word_list, 5)
        while(True):
            if self.num_lives < 0 :
                print("You lost!")
                break
            if self.num_letters > 0:
                self.ask_for_input()
            if self.num_lives > 0 and self.num_letters < 1:
                print("You won!!")
                break

if __name__=="__main__":
    play = Game()
    play.play_game()


            

