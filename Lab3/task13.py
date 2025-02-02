import random

def guess_number(name, number, guesses=0):
    print("Take a guess.")
    guess = int(input())
    guesses += 1
    if guess < number:
        print("\nYour guess is too low.")
        return guess_number(name, number, guesses)
    elif guess > number:
        print("\nYour guess is too high.")
        return guess_number(name, number, guesses)
    else:
        print(f"\nGood job, {name}! You guessed my number in {guesses} guesses!")
        return

def main():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guess_number(name, number)

main()
