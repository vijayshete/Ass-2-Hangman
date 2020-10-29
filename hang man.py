import time
import random

name = input("What is your name ?")
print("Hello " + name)
print("Time to play")

time.sleep(1)

print("Start guessing... : ")
time.sleep(0.5)

words = ["mango", "quine", "sparrow", "grass", "door", "donkey", "peacock", "pencil", "house", "happy", "college", "basket",
         "galaxy", "lotus", "table", "mouse", "food", "bottle", ]
n = random.randint(0, 17)
word = words[n]
guesses = ""

turns = 5

while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(" ",char)
        else:
            print("  _  ")
            failed += 1

    if failed == 0:
        print("YOU WON ",name," !!!")
        break
    guess = input("Guess a letter :")
    guesses += guess[0]
    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have", +turns, "more guesses")

    if turns == 0:
        print("YOU LOOS ",NAME," !!!")

print("The word is : ", word)
