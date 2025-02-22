import random
import os

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = int(os.getenv("ATTEMPTS", "5"))

    print(f"Guess the number game! The number is between 1 and 100.")
    for _ in range(attempts):
        guess = random.randint(1, 100)  # Automatic guess generation
        print(f"Guessing: {guess}")

        if guess < number_to_guess:
            print("Too Low!")
        elif guess > number_to_guess:
            print("Too High!")
        else:
            print(f"Congratulations! You are right, the number is {number_to_guess}.")
            break
    else:
        print(f"Failed to guess the number in {attempts} attempts. It was {number_to_guess}.")

if __name__ == "__main__":
    guess_number()
