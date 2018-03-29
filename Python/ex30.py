# This exercise is Part 1 of 3 of the Hangman exercise series. The other exercises are: Part 2 and
# Part 3.
# In this exercise, the task is to write a function that picks a random word from a list of words
# from the SOWPODS dictionary.

import random

with open('/home/phaldox/Downloads/sowpods.txt', 'r') as wordbook:
    database = wordbook.readlines()

def pickWord():
    number = random.randint(0, len(database))
    word = database[number]
    return word



#Ex31

def Hangman():
    guess = 0
    answer = 0
    word = pickWord()
    used = []

    print(word) #debug

    for x in word:
        answer += ord(x)
    while(guess != answer):
        g = raw_input("Guess a letter: ")
        if g in word:

            used.append(g)



print(Hangman())
