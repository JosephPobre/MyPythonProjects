import random

number = random.randint(1,100)
user_input = 0

while user_input != number:
    user_input = int(input("Enter a guess: "))

    if (user_input < number):
        print("Guess higher!")
    elif (user_input > number):
        print("Guess lower!")
    else:
        print("You won!")
