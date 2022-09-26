import random
import string




class test:

    def get_random(self, fruits: list):
        """Return a random item froma list 
        :input: list
        :return: object"""
        return print(random.choice(fruits))

    def ask_input(self):
        guess=input("Please input a letter name: ")
        if len(guess) == 1 :
            print()
        else:
            print("Please input only one letter!")
            guess = input("Input your letter again: ")
        return print("Your input was %s"% guess)
            


if __name__=="__main__":
    fruits=["strawberry","apple","kiwi","banana","mango"]
    t = test()
    t.get_random(fruits)
    t.ask_input()
