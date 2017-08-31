'''
COPY THIS CODE TO YOUR IDE TO SEE IF YOU CAN GUESS THE NUMBER!!!

'''

# Simple guess the number game
# 1. Write your name
# 2. Write the level of the game : 1 level - 1-10 range; 2 level - 1-100 range; 3 level - 1-1000 range
# 3. Guess the number and have fun :)

# importing random to get the function - randint
import random as rnd
import time as tm


# Definition a function with a lvl 1 conditions for a game
def level_lvl(level):
    if level == 1:
        # answer is a random generated number for specify range
        answer = rnd.randint(1, 10)
        # The range of this level
        print("Enter your number from 1-10 range to guess the number:")
    elif level == 2:
        # answer is a random generated number for specify range
        answer = rnd.randint(1, 100)
        # The range of this level
        print("Enter your number from 1-100 range to guess the number:")
    elif level == 3:
        # answer is a random generated number for specify range
        answer = rnd.randint(1, 1000)
        # The range of this level
        print("Enter your number from 1-1000 range to guess the number:")

    elif level == 0:
        print("BAD")
        return None
    # guess is a variable to be input by the player
    guess = int(input())
    #after giving a number the game is started
    start = tm.time()
    # variable times is to count how many attempts player have done to win the game at a specify game level
    times = 1
    # This is a exception that player win the game after first attempt
    if guess == answer:
        # This is the clock of the game
        timer = (tm.time() - start)
        print("WOW {0}! You have done it after {1} times!? \n"
              "Congratulations!"
              "You have passed {2} level of the game in {3} seconds.".format(name, times, level, timer))
    # while loop is practital for this part of the game
    while guess != answer:
        # times gets +1 because next guess is already counted
        times += 1
        if guess < answer:
            print("HIGHER! {} HIGHER!!!".format(name))
        else:
            print("LOWER!! {} LOWER!!!!".format(name))
        # after not guessing the number player have another chance
        guess = int(input())
        # if player guess the number, program will end and give the
        if guess == answer:
            # This is the clock of the game
            timer = (tm.time() - start)
            print("YES {0}! You have done it!"
                  "\nThe number you were guessing was {3}!"
                  "\nYou get your score after {1} times on {2} level in {4:2} seconds.".format(name, times, level,
                                                                                               answer, timer))
            # break will end with if and while and go to the last line of the code
            break
name = input("Please write your name: ")
print(name + " Welcome to Guess the number game!\n"
             "Level 1: 1-10 range\n"
             "Level 2: 1-100 range\n"
             "Level 3: 1-1000 range\n")
level = int(input("What level you want to play?: "))
level_lvl(level)
print("\n\nYou have played in Łukasz Obiedziński game called - Guess the number."
      "\nIf you like it please upvote this and have a nice day:)")
