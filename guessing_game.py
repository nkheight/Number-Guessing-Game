import random

attempts = []

def add_attempt(number):
  attempts.append(number)

def start_game():
    print("Welcome to \"Can You Guess the Number?\"")
    player_name = input("Please enter your name: ")
    print("Instructions: {} guess a number between 1 and 100!".format(player_name))

answer = random.randint(1, 100)

start_game()
while True:
    try:
    guess = int(input("Enter your guess: "))
        if guess > 100:
            raise ValueError("Guess has to be a number between 1 and 100")
        elif guess < 1:
            raise ValueError("Guess has to be a number between 1 and 100")
            
    except ValueError as err:
        print("That is not a valid value")
    
    else:
        if guess == answer:
          print("You got it!")
          break
        elif guess > answer:
          print("It's lower.")
          continue
        elif guess < answer:
          print("It's higher.")
          continue