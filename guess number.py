import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess what it is?")

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("\nEnter your guess (or 'exit' to end the game): ")

        # Allow the player to exit the game
        if guess.lower() == 'exit':
            print(f"The secret number was {secret_number}. Goodbye!")
            break

        # Check if the input is a valid number
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number or 'exit'.")
            continue

        # Increment attempt counter
        attempts += 1

        # Provide hints
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed it right in {attempts} attempts.")
            break

    print("\nThanks for playing!")

if __name__ == "__main__":
    guessing_game()


