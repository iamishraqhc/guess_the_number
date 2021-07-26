import random

number = random.randint(1,10)
tries = 3
for i in range(0,tries):
    user = int(input("Guess the number: "))
    if user == number:
        print("Awesome!!")
        print(f"You have guessed the number right. It's {number}")
        break
    else:
        tries = tries - 1
        print(f"Tries left:  {tries}")
if user != number:
    print(f"Sorry, your guesses were incorrect. The number is {number}")
    