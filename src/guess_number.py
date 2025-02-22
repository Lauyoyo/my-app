
import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Guess the numbers game! The numbers are between 1 and 100.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number_to_guess:
            print("Too Low！")
        elif guess > number_to_guess:
            print("Too High！")
        else:
            print(f"Congratulations! You are right, the number is {number_to_guess}。You used {attempts} attempts。")
            break

if __name__ == "__main__":
    guess_number()